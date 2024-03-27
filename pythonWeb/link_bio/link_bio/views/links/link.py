import reflex as rx 

from link_bio.components.link_button import linkButton
def links() -> rx.Component:
    return rx.vstack(
        linkButton("Linkedin", "https://www.linkedin.com/in/juandavidsernamolina/"),
        linkButton("Github","https://github.com/juansm1664"),
        linkButton("Instagram","https://www.instagram.com/juandasernam/"),
        linkButton("X" ,"https://twitter.com/juandasernam")
    )
