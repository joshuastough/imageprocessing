## imageprocessing
### [Joshua Stough](http://joshuastough.com), 202-

Imaging is everywhere! In this text, we will cover broadly the acquisition, processing, and analysis of digital images, covering topics ranging from the human visual system, to image and video compression algorithms, to pattern recognition and machine learning within the context of automatic image understanding. Best of all, for the sake of access, immediacy, and usability, all content and code examples are in the form of interactive Jupyterlab notebooks!

***This book is still under construction. But the interactive visualizations work in binder without a time-consuming local install! Come check it out below!***

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/joshuastough/imageprocessing/HEAD?filepath=TOC.ipynb)

- [Creating a private fork of this project](private_fork_instructions.md)
- Installing a local virtual environment supporting this textbook
 1. [Get Anaconda](https://docs.anaconda.com/anaconda/)
 1. [Set up a conda env](https://medium.com/swlh/setting-up-a-conda-environment-in-less-than-5-minutes-e64d8fc338e4) with this [requirements.txt](./requirements.txt)

I am writing a book on introductory image processing in [Python](https://www.python.org/about/). For the sake of immediacy and usability, all content and code examples are in the form of IPython notebooks that execute through [binder](https://mybinder.org/)!


&nbsp;
&nbsp;

Opening in Colab: There's a bit of additional hassle getting this textbook working in Colab. But the payoff is that you can [link to your private fork of this project](https://colab.research.google.com/github/googlecolab/colabtools/blob/main/notebooks/colab-github-demo.ipynb) to save your work, without ever having to install a local environment. 
To every notebook that begins with `%matplotlib widget` you should:

- Insert a Code cell at the top and execute `!pip install ipympl`. This will install [ipympl](https://github.com/matplotlib/ipympl) in your Colab session, for producing interactive plots. 
- Then, insert a Code cell after with 
```python
from google.colab import output
output.enable_custom_widget_manager()
```

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/joshuastough/imageprocessing/blob/main/TOC.ipynb)