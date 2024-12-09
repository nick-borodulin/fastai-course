# AUTOGENERATED! DO NOT EDIT! File to edit: ../bear_classifier_gratio.ipynb.

# %% auto 0
__all__ = ['learn_inf', 'categories', 'image', 'label', 'examples', 'interface', 'classify_image']

# %% ../bear_classifier_gratio.ipynb 1
from fastai.vision.all import *
import gradio as gr

# %% ../bear_classifier_gratio.ipynb 2
learn_inf = load_learner('bears.pkl')

# %% ../bear_classifier_gratio.ipynb 3
categories = learn_inf.dls.vocab

def classify_image(img):
    prediction,_,probability = learn_inf.predict(img)
    return dict(zip(categories, map(float, probability)))

# %% ../bear_classifier_gratio.ipynb 4
image = gr.Image(height=192, width=192)
label = gr.Label()
examples = ['black.jpg', 'grizzly.jpeg', 'teddy.jpeg']
interface = gr.Interface(fn=classify_image, inputs=image, outputs=label, examples=examples)
interface.launch(inline=False)
