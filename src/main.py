from flet import *
from commands import FileReader, MainCommands


def main(page: Page):
    page.rtl = True
    page.baseUrl = "https://apiv2.clappia.com"

    page.window.width = 1000
    page.window.height = 800
    page.window.resizable = False
    page.window_maximizable = False
    page.window_minimizable = False

    page.fileReader = FileReader(page)
    page.mainCommandes = MainCommands(page)

    # page.client_storage.get_async

    page.appbar = AppBar(
        title=Text("مرحبا بك في مدخل البيانات"),
        bgcolor="#666666",
        actions=[
            IconButton(icon=Icons.PERSON, on_click=page.mainCommandes.addTockinTextBox)
        ],
    )

    page.theme_mode = ThemeMode.DARK
    page.theme = Theme(text_theme=TextTheme(body_large=TextStyle(color="#fff")))

    pick_files_dialog = FilePicker(on_result=page.fileReader.pick_files_result)
    page.overlay.append(pick_files_dialog)

    page.floating_action_button = FloatingActionButton(
        icon=Icons.ADD,
        on_click=lambda _: pick_files_dialog.pick_files(
            allow_multiple=True,
            allowed_extensions=["xlsx"],
            dialog_title="اختر مجموعة الملفات",
        ),
    )

    page.succesTableRef = Ref[DataTable]()
    page.FiledTableRef = Ref[DataTable]()
    page.startButton = Ref[TextButton]()
    page.puseButton = Ref[TextButton]()
    page.stopButton = Ref[TextButton]()

    page.add(
        SafeArea(
            ResponsiveRow(
                controls=[
                    Container(
                        content=Text(
                            "العدادت التي تم ادخالها",
                            style=TextStyle(weight=FontWeight.BOLD, size=17),
                        ),
                        width=float("inf"),
                        padding=padding.symmetric(vertical=10, horizontal=20),
                    ),
                    Container(
                        Column(
                            controls=[
                                DataTable(
                                    columns=[
                                        DataColumn(Text("submissionId")),
                                        DataColumn(Text("اسم الملف")),
                                        DataColumn(Text("مسار الملف"), numeric=True),
                                    ],
                                    
                                    width=float("inf"),
                                    ref=page.succesTableRef,
                                ),
                            ],
                            scroll=ScrollMode.ALWAYS,
                            expand=True,
                        ),
                        alignment=alignment.center,
                        width=float("inf"),
                        padding=padding.symmetric(vertical=10, horizontal=20),
                        height=200
                    ),
                    Container(
                        content=Text(
                            "العدادت التي فشلت ",
                            style=TextStyle(weight=FontWeight.BOLD, size=17),
                        ),
                        width=float("inf"),
                        padding=padding.symmetric(vertical=10, horizontal=20),
                    ),
                    Container(
                        Column(
                            controls=[
                                DataTable(
                                    columns=[
                                        DataColumn(Text("submissionId")),
                                        DataColumn(Text("اسم الملف")),
                                        DataColumn(Text("مسار الملف"), numeric=True),
                                    ],
                                    width=float("inf"),
                                    ref=page.FiledTableRef,
                                ),
                            ],
                            scroll=ScrollMode.ALWAYS,
                            expand=True,
                        ),
                        alignment=alignment.center,
                        width=float("inf"),
                        padding=padding.symmetric(vertical=10, horizontal=20),
                        height=200
                    ),
                    Container(
                        content=Row(
                            controls=[
                                Container(
                                    content=TextButton(
                                        text="بدء",
                                        icon=Icons.START,
                                        on_click=page.mainCommandes.startAdd,
                                        ref=page.startButton,
                                        disabled=True,
                                    ),
                                    width=300,
                                    height=50,
                                    border=border.all(color="#dddddd", width=0.1),
                                    border_radius=border_radius.all(40),
                                ),
                                Container(
                                    content=TextButton(text="ايقاف", icon=Icons.PAUSE),
                                    width=300,
                                    height=50,
                                    border=border.all(color="#dddddd", width=0.1),
                                    border_radius=border_radius.all(40),
                                    ref=page.stopButton,
                                    disabled=True,
                                    on_click=page.mainCommandes.stopAdd
                                ),
                            ],
                            alignment=MainAxisAlignment.CENTER,
                        ),
                        padding=padding.all(20.0),
                    ),
                ]
            ),
            expand=True,
        )
    )


app(main, assets_dir="/assets")
