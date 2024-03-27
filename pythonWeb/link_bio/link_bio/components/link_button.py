import reflex as rx 


def linkButton(text: str, url: str)-> rx.Component:
    return rx.link(
        rx.button(text),
        href = url,
        is_external =True
    )
       