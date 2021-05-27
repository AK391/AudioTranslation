import gradio as gr
from gradio.mix import Parallel, Series

io0 = gr.Interface.load("huggingface/facebook/wav2vec2-base-960h")
io1 = gr.Interface.load("huggingface/facebook/m2m100_418M")

Series(io0, io1).launch()