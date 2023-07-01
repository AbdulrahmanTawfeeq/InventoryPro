import tkinter as tk


def clear_form(form):
    # Iterate over the attributes of the form object
    for attr_name in dir(form):
        attr_value = getattr(form, attr_name)
        if isinstance(attr_value, tk.Entry):
            attr_value.delete(0, tk.END)
