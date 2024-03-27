import reflex as rx

def navbar()-> rx.Component:
    return rx.hstack(                   #Component para elementos horizontales
            rx.text(
                "Juan David",
                height = "40px"
            ),
            position ="sticky",
            bg="red",
            padding_x= "16px",
            padding_y= "30px",
            z_index = "999"       
        )