# app.py - Gradio web interface for Hugging Face Spaces
import gradio as gr

def add(a, b):
    """Returns the sum of a and b."""
    return a + b

def string_add(a, b):
    """Returns the concatenation of a and b."""
    return a + b

# Gradio Interface for Number Addition
number_interface = gr.Interface(
    fn=add,
    inputs=[
        gr.Number(label="First Number (a)"),
        gr.Number(label="Second Number (b)")
    ],
    outputs=gr.Number(label="Sum (a + b)"),
    title="Number Addition",
    description="Enter two numbers to add them together."
)

# Gradio Interface for String Concatenation
string_interface = gr.Interface(
    fn=string_add,
    inputs=[
        gr.Textbox(label="First String (a)", placeholder="Hello"),
        gr.Textbox(label="Second String (b)", placeholder="World")
    ],
    outputs=gr.Textbox(label="Concatenated String"),
    title="String Concatenation",
    description="Enter two strings to concatenate them."
)

# Combine both interfaces in tabs
demo = gr.TabbedInterface(
    [number_interface, string_interface],
    ["Number Addition", "String Concatenation"],
    title="Addition Functions Demo"
)

if __name__ == "__main__":
    demo.launch()