# Using Generative Adversarial Networks for inversion of Geophysical data

This project explores the feasability of using Generative Adversarial Networks (GAN's) in the pipeline for solving Geophysical problems. This is an extension on the work done by  <cite>[Laloy et al., 2019][1]</cite>. Laloy in his paper explores the fesability of using GAN's to aid in the inversion process for geophysical problems. The idea is to learn the latent representation of the distribution of 

## Table of contents
1. [Installation](#installation)
3. [Background Information](#Background-Information)    
4. [Implementation](#implementation)




## Installation <a name="installation"></a>

```
$ git clone https://github.com/akhilnas/geophysical-inversion.git
$ cd geophysical-inversion/
$ sudo pip3 install -r requirements.txt
```

## Background Information <a name="#Background-Information"></a>




## Implementation <a name="implementation"></a>

The Python Script with the base parameters is run with the following command in Terminal.

```
$ python main.py 
```
To use different parameters to execute the training of the model the following command illustrates the modifiable parameters.

```
$ python main.py --n_epochs <Epoch> --batch_size <Batch Size> --lr <Learning Rate> --b1 <Adam Parameter> --b2 <Adam Parameter> --n_cpu <CPU Threads>
--latent_dim <Latent Dimension> --img_size <Image Size> --channels <Channels> --sample_interval <Image Sample Interval>
```

The Code can also be implemented with the help of Docker. For instruction on Docker Installation please see [here][1]. The Docker Implementation is available on [Docker Hub][2].

[1]: https://docs.docker.com/get-docker/
[2]: https://hub.docker.com/r/akhiln/gan-stable


```
$ docker pull akhiln/gan-stable
```


[1]: https://arxiv.org/abs/1812.09140
