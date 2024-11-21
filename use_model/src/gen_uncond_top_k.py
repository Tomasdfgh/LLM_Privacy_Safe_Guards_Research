#!/usr/bin/env python3

import fire
import json
import os
import numpy as np
import tensorflow as tf
import model, sample, encoder

def count_files(directory):
    return len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))])

def sample_model(
    model_name='124M',
    seed=None,
    batch_size=1,
    length=256,
    temperature=1,
    top_ks=[0, 10, 50, 100, 200, 500, 1000],
    top_p=1,
    models_dir='models',
    num_files_per_k=10000,
    output_base_dir=r'C:\Users\tomng\Desktop\Dataset\top_k'
):

    models_dir = os.path.expanduser(os.path.expandvars(models_dir))
    enc = encoder.get_encoder(model_name, models_dir)
    hparams = model.default_hparams()
    with open(os.path.join(models_dir, model_name, 'hparams.json')) as f:
        hparams.override_from_dict(json.load(f))

    if length is None:
        length = hparams.n_ctx
    elif length > hparams.n_ctx:
        raise ValueError("Can't get samples longer than window size: %s" % hparams.n_ctx)

    for top_k in top_ks:

        path_label = os.path.join(output_base_dir, f"{top_k}")
        num_files = count_files(path_label)
        if num_files < num_files_per_k:

            with tf.Session(graph=tf.Graph()) as sess:
                np.random.seed(seed)
                tf.set_random_seed(seed)

                output = sample.sample_sequence(
                    hparams=hparams, length=length,
                    start_token=enc.encoder['<|endoftext|>'],
                    batch_size=batch_size,
                    temperature=temperature, top_k=top_k, top_p=top_p
                )[:, 1:]

                saver = tf.train.Saver()
                ckpt = tf.train.latest_checkpoint(os.path.join(models_dir, model_name))
                saver.restore(sess, ckpt)

                generated = num_files
                while generated < num_files_per_k:
                    out = sess.run(output)
                    for i in range(batch_size):

                        generated += batch_size
                        text = enc.decode(out[i])
                        path_save = os.path.join(path_label, f"{generated}.txt")

                        with open(path_save, 'w', encoding='utf-8') as f:
                            f.write(text)

if __name__ == '__main__':
    fire.Fire(sample_model)