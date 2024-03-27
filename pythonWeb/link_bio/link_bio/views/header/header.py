import reflex as rx 

def header() -> rx.Component:
    return rx.vstack(
            rx.avatar(fallback="JD", size="3", variant = "solid" , hight_contract = True, color_scheme="indigo"),
            rx.text("@juanda1664"),
            rx.text("Hola linkBio de Juan David Serna molina"),
            rx.text("""Bilingual computer and systems engineering professional 
                    (B2 in English) with the ability to design software projects 
                    and manage computer resources""")
        )