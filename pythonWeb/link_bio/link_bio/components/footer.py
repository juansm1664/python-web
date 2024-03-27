import reflex as rx 
import datetime

def footer() -> rx.Component:
    return rx.vstack(
            rx.image(
                src = "favicon.ico"),
            rx.link(f"Perfil de Github -{datetime.date.today().year}", #Concardenación f antes del string
                    href="https://github.com/juansm1664",
                    is_external=True),
            rx.text("""💬 I'm interested in: software engineering, web development, 
                 cloud architecture, artificial intelligence.""")
    )
    
    
    
    