import flet as ft
import speedtest
from time import sleep
from TypewriterEffectControl import TypeWriterControl




def main(page:ft.Page):
   #setting the page
   page.title = "Internet speed test"
   page.theme_mode = "dark"
   page.horizontal_alignment = "center"
   page.vertical_alignment = "center"
   page.window_bgcolor ="blue"
   page.padding = 30
   page.bgcolor ="black"
   
   #enable scroll in the page
   
   page.auto_scroll =True
   
   #define font application
   page.fonts = {
        "RoosterPersonalUse":"fonts/RoosterPersonalUse-3z8d8.ttf",
        "SourceCodeProBlackItalic":"fonts/SourceCodePro-BlackItalic.ttf",
        "SourceCodeProBold": "fonts/SourceCodePro-Bold.ttf"
   }
   
   #unitialising the speedtest module
   
   st = speedtest.Speedtest()
   
   #making the heading of app
   
   appTitle = ft.Row(
       controls=[
           ft.Text("Internet", font_family="RoosterPersonalUse",color="yellow",size=45,theme_style=ft.TextThemeStyle.DISPLAY_LARGE),
           ft.Text("Speed", font_family="RoosterPersonalUse",color="red",size=45,theme_style=ft.TextThemeStyle.DISPLAY_LARGE)
       ],
       alignment="center"       
   )
  
   #define lines of terminal printing text
 
   line_01 = TypeWriterControl(value=">press start...",font_family= "SourceCodeProBlackItalic",color="#ffffff")
   line_02 = TypeWriterControl(value="",font_family= "SourceCodeProBlackItalic",color="#80ff00")
   line_03 = TypeWriterControl(value="",font_family= "SourceCodeProBlackItalic",color="#80ff00")
   Progressbar_01 = ft.ProgressBar(width=400,color="#0080ff",bgcolor="white",opacity=0)
   progress_text_01 = TypeWriterControl(value=" ",font_family="SourceCodeProBlackItalic",transparency=False)
   progress_row_01 = ft.Row([progress_text_01,Progressbar_01])
   line_04 = TypeWriterControl(value="",font_family= "SourceCodeProBold ",color="yellow")
   line_05 = TypeWriterControl(value="",font_family= "SourceCodeProBlackItalic",color="#80ff00")
   line_06 = TypeWriterControl(value="",font_family= "SourceCodeProBlackItalic",color="#80ff00")
   Progressbar_02 = ft.ProgressBar(width=400,color="#0080ff",bgcolor="white",opacity=0)
   progress_text_02 = TypeWriterControl(value=" ",font_family="SourceCodeProBlackItalic",transparency=False)
   progress_row_02 = ft.Row([progress_text_02,Progressbar_02])
   line_07 = TypeWriterControl(value="",font_family= "SourceCodeProBold",color="yellow")
   line_08 = TypeWriterControl(value="",font_family= "SourceCodeProBlackItalic",color="#ffffff")
   
   terminalText =ft.Column([line_01,line_02,line_03,Progressbar_01,line_04,line_05,line_06,Progressbar_02,line_07,line_08]) 
   
   getSpeedContainer = ft.Container(
       content=terminalText,
       width=200,
       height=100,
       bgcolor="#808080",
       border_radius=30,
       padding=20,
       animate=ft.animation.Animation(1000,"bounceOut")
   )
      #terminal container
      
   def animate_getSpeedContainer(e):
       progress_row_01.opacity = 0
       Progressbar_01.opacity = 0
       Progressbar_01.value=None       
       progress_row_02.opacity = 0
       Progressbar_02.opacity = 0
       Progressbar_02.value=None       
       line_01.text_to_print = ""
       line_01.update()
       line_02.text_to_print = ""
       line_02.update()
       line_03.text_to_print = ""
       line_03.update()
       line_04.text_to_print = ""
       line_04.update()
       line_05.text_to_print = ""
       line_05.update()
       line_06.text_to_print = ""
       line_06.update()
       line_07.text_to_print = ""
       line_07.update()
       line_08.text_to_print = ""
       line_08.update() 
       getSpeedContainer.update()
       getSpeedContainer.width=700
       getSpeedContainer.height =400
       line_01.text_to_print=">calculating download speed, please wait..."
       getSpeedContainer.update()
       sleep(1)
       line_01.update()
       
       ideal_server = st.get_best_server() #this will be able to find and connect to best possible server in your region 
       city = ideal_server["name"]
       country = ideal_server["country"]
       cc = ideal_server["cc"]
       line_02.text_to_print = f">finding the best possible server in {city}, {country} ({cc})"
       getSpeedContainer.update()
       sleep(2)
       line_02.update()
       
       line_03.text_to_print = "> connexion established, status Ok, fetching download speed"
       line_03.update()
       progress_row_01.opacity=1
       Progressbar_01.opacity=1
       getSpeedContainer.update()
       #sleep(2)       
       download_speed = st.download()/1024/1024 #bytes/sec to Mbps       
       Progressbar_01.value=1
       
       line_04.text_to_print= f"> the download speed is {str(round(download_speed,2))} Mbps"
       line_04.update()
       getSpeedContainer.update()
       #sleep(2)
       
       line_05.text_to_print=">calculating upload speed, please wait..."
       line_05.update()
       getSpeedContainer.update()
       sleep(1)
       
       line_06.text_to_print=">executing upload script, hold on"
       line_06.update()
       progress_row_02.opacity=1
       Progressbar_02.opacity=1
       getSpeedContainer.update()
       upload_speed = st.upload()/1024/1024 # bytes/sec to Mbps
       Progressbar_02.value =1
       
       line_07.text_to_print= f"> the upload speed is {str(round(upload_speed,2))} Mbps"
       line_07.update()
       getSpeedContainer.update()
       sleep(1)
       
       line_08.text_to_print = ">task completed successfully\n\n>>> app developer : Fulgence nahimana (instagram:https://www.instagram.com/nahimanafulgence)"
       line_08.update()
       getSpeedContainer.update()
       
   page.add(
      appTitle,
      getSpeedContainer,
      ft.IconButton(icon=ft.icons.PLAY_CIRCLE_OUTLINED,icon_color="green",icon_size=50,on_click=animate_getSpeedContainer),
      
   )




ft.app(target=main,assets_dir="assets")