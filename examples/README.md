## Setting up the repository

### Cloning the submodules

When cloning the repository, you will need to run the following command to set up the repositories:
may need to first run the following line if one ROSIE `git submodule sync`
`git submodule update --init --recursive`

This will add in the submodules, and link them to our repository. The submodule is just a link from our repository to another repository, which allows for us to easily use their code within our project. 

To be safe, you can run this following command when in the main `Discovery-World-Face-GAN` folder:

`cd ./examples/ganspace; git submodule update --init --recursive; cd ../stylegan2-local; git submodule update --init --recursive`

This shouldn't be needed, but in case the repositories aren't initialized, it will go into each and pull in any submodules they contain. 

**NOTE:** If running on linux (or in Windows bash), replace the `;` with `&&` to make all commands run

### Installing Anaconda 

[Install Anaconda](https://www.anaconda.com/products/individual) if you don't have it already. Through this setup, you can either configure it to work through *Anaconda Prompt* (which is what they recommend - you will need to launch the project in Anaconda Prompt to get it to work correctly though), or in any shell through your path. If you have questions about adding it to path so you can use it in other prompts (like cmd or powershell), reach out to the team.

Make sure you run `conda activate ganspace` before running any of the commands below to make sure the project has access to the dependencies it needs.

### Setting up GANSpace

[Follow the GANSpace setup instructions](https://github.com/NathanDuPont/ganspace/blob/65b0c4c7a4bbdcb5fedebb7c033dab59e27d61c0/SETUP.md) located in the submodule (./examples/ganspace/SETUP.md). These will take you through the needed installations. When installing the files in the *deps* directory, you may need to change it from running the entire folder to running each file one at a time.

Once the installation is complete, go back to the [GANSpace Readme](https://github.com/NathanDuPont/ganspace/blob/65b0c4c7a4bbdcb5fedebb7c033dab59e27d61c0/README.md) and run any of the commands provided. Start with this one to check if the program works:

```
# Explore StyleGAN2 ffhq in W space
python interactive.py --model=StyleGAN2 --class=ffhq --layer=style --use_w -n=1_000_000 -b=10_000
```

**NOTE:** Make sure you're in the `ganspace` folder when executing the command above or it will not run.


---

## Examples of GAN Facial Augmentation


### DC-GAN

[Medium Article](https://medium.com/using-deep-learning-dc-gan-to-add-featured-effect/recently-i-started-the-creative-applications-of-deep-learning-with-googles-tensorflow-of-parag-k-14453b215d2b)

[Source Code](https://github.com/Kjeanclaude/CADL-I-FinalPoject)

Notes: 

This GAN allows for adding and modifying features on an individuals face, but also has a blurring effect that removes lots of details from the end results. This may be good for testing, but for final implementation this might not work well.

### Transparent Latent GAN

[Medium Article](https://medium.com/p/d170b1b59255)

[Project Demo on Kaggle (broken)](https://www.kaggle.com/summitkwan/tl-gan-demo)

[Source Code](https://github.com/SummitKwan/transparent_latent_gan)

Notes: 
This network does a good job at producing realistic images, but currently only supports generating new faces from a random vector input. The accompanying articles provide good detail to describe modifications to latent vectors of faces within the model, and could be used with this model or others.

### Face Attribute Manipulation using GANs

[Towards Data Science Article](https://towardsdatascience.com/face-attribute-manipulation-using-gans-9fae92e9f1c3)

[Paper](https://arxiv.org/pdf/1612.05363.pdf)

[Source Code](https://github.com/MingtaoGuo/Learning-Residual-Images-for-Face-Attribute-Manipulation)


Notes: While this model can produce decent resolution outputs, there are lots of artifacts remaining from the original features and will likely not be usable in a final model. However, it does allow for modifying multiple different attributes with examples, and performance may be able to be boosted with modifications


### iSee - Removing glasses

[Article](https://blog.insightdatascience.com/isee-removing-eyeglasses-from-faces-using-deep-learning-d4e7d935376f#.v3iw0prqo)

Notes: This guide has lots of good information about developing these models from open-source code, but doesn't have as much code with the article

### Miscellaneous Articles
 
[Building Web Apps with PyTorch Models](https://medium.com/plotly/building-apps-for-editing-face-gans-with-dash-and-pytorch-hub-1e7026c0bc9a)
