def clear_window_content(window):
    for widget in window.winfo_children():
        if widget.winfo_class() != 'Menu':
            widget.destroy()
