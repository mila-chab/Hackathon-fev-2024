import flet as ft


def la_page(page):
    t = ft.Text(value="ouais ouais ouais c le wei", color = "green")
    page.controls.append(t)
    page.update()

ft.app(target=la_page)



"""
page.add(
    ft.Column([
      ### header
      ft.Row([
        # message area
        ft.TextField(...)
      ]),
      ft.GridView(
        # the 9 digits
        [ ft.Button(...), ..., ft.Button(...)]),
      # footer
      ft.Row([
         # the 4 buttons
         ft.IconButton(...), ..., ft.IconButton(...)]),
      )
    ]
  )
  """