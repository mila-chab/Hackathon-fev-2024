import flet as ft
import time

SIZE = 3

def la_page(page):
    t = ft.Text(value="ouais ouais ouais c le wei", color = "green")
    page.controls.append(t)
    page.update()
    t= ft.Text()
    page.add(t)

    for i in range(2):
      t.value = f"step {i}"
      page.update()
      time.sleep(1)
    
    ligne = ft.Row(controls = [ft.TextField(label = 'ton prénom'), 
                               ft.ElevatedButton(text= 'dis ton nom!')])
    page.add(ligne)
    container = ft.Container(
        width=200,
        height=200,
        #border=ft.border.all(1, ft.colors.BLACK),
        bgcolor='#ff0030',
        content=ft.FilledButton("Primary color"),
        theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.YELLOW)))
    
    page.add(container)




#ft.app(target=la_page)

def bienvenue(page):
    greetings = ft.Text(value = 'Bienvenue sur le jeu du taquin.\nAmusez-vous bien', color = 'ff0000')
    page.add(greetings)
    
    #greetings.disabled = True
    #page.add(greetings)


def affichage(page):
    larg = 150
    r = ft.Row(wrap=True, scroll="always", expand=False)
    page.add(r)

    for i in range(SIZE**2):
        r.controls.append(
            ft.Container(
                ft.Text(f"Item {i}", color =  "black"),
                width=larg,
                height=larg,
                alignment=ft.alignment.center,
                bgcolor="#dc4922",
                border=ft.border.all(1, "000000"),
                border_radius=ft.border_radius.all(37),
            )
        )
        if i%SIZE == SIZE-1:
          r = ft.Row(wrap=True, scroll="always", expand=False)
          page.add(r)

  
#ft.app(target = bienvenue)
ft.app(target = affichage)


"""
t = ft.Column([
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
page.add(t)
  """