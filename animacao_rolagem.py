import flet as ft 
def main(page:ft.Page):
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.bgcolor=ft.colors.BLACK
    def move_esquerda(e):
        imagens.scroll_to(delta=-100,duration=300,curve=ft.AnimationCurve.DECELERATE)
        imagens.update()
    def mover_direita(e):
        imagens.scroll_to(delta=+100,duration=300,curve=ft.AnimationCurve.DECELERATE)
    layout=ft.Container(
        shadow=ft.BoxShadow(blur_radius=150,color=ft.colors.CYAN),
        content=ft.Column(
            controls=[
               imagens:= ft.Row(
                    controls=[
                        ft.Image(
                            src=f'https://picsum.photos/200/200?{num}'
                        )for num in range(0,100)
                    ],scroll=ft.ScrollMode.HIDDEN,
                ),
                ft.Row(
                    controls=[
                        ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_LEFT,on_click=move_esquerda,bgcolor=ft.colors.BLACK),
                        ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_RIGHT,on_click=mover_direita,bgcolor=ft.colors.BLACK)
                    ],alignment=ft.MainAxisAlignment.END,
                )
            ]
        )
    )
    page.add(layout)
if __name__=="__main__":
    ft.app(target=main)