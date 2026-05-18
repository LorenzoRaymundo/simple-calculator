import customtkinter as ctk

# frame 0: title
# frame 1: result
# frame 2: btns

class CalculatorApp:

    def __init__(self):

        ''' CONSTANTS '''
        self.APP_WIDTH = 320
        self.APP_HEIGHT = 540

        self.STD_FONT = "Arial"
        self.STD_FONT_SIZE = 24

        self.BTN_SIZE = 40

        self.BG_COLOR = "#1E1E1E"
        self.FRAME_COLOR = "#2B2B2B"

        self.NUMBER_BTN = "#3A6FF7"
        self.NUMBER_HOVER = "#5A86FF"

        self.OP_BTN = "#505050"
        self.OP_HOVER = "#686868"

        self.DISPLAY_COLOR = "#151515"

        self.error_flag = False
        # main window
    
        self.wdw = ctk.CTk()
        self.wdw.title("Simple calc")
        self.wdw.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}")
        self.wdw._set_appearance_mode("dark")
        self.wdw.configure(fg_color=self.BG_COLOR)

        self.equation_display = ctk.StringVar(self.wdw, value="0") # ctk var that ill be using to display the equation
        self.buffer : str = "" # python var that ill be using to build an equation

        self.main_title = ctk.CTkLabel(
            self.wdw,
            text="Calculator",
            font=(self.STD_FONT, 18, "bold"),
            text_color="#A0A0A0"
        )
        self.main_title.pack(fill="both", padx=10, pady=(15, 10))


        self.res_frame = ctk.CTkFrame(
            self.wdw,
            height=self.APP_HEIGHT/8, # type: ignore
            fg_color=self.FRAME_COLOR,
            corner_radius=20
        )
        self.res_frame.pack(fill="both", padx=20, pady=(0, 20))

        self.display = ctk.CTkEntry(
            self.res_frame,
            textvariable=self.equation_display,
            font=(self.STD_FONT, 32, "bold"),
            justify="right",
            border_width=0,
            fg_color=self.DISPLAY_COLOR,
            corner_radius=15
        )
        self.display.pack(expand=True, fill='both', padx=10, pady=10, side="right")


        self.btns_frame = ctk.CTkFrame(
            self.wdw,
            fg_color="transparent"
        )
        self.btns_frame.pack(fill="y", padx=(20, 10), pady=10, side="left")

        self.operations_frame = ctk.CTkFrame(
            self.wdw,
            fg_color="transparent"
        )
        self.operations_frame.pack(padx=(10, 20), pady=10, side='right', fill='both')

    def update_display(self, n : str):
        if n == "C":
            self.buffer = ""
        else:
            if n == " = ":
                try:
                    print(self.buffer)
                    self.buffer = str(eval(self.buffer.replace("x", "*").replace("÷", "/"))) # main logic
                except:
                    self.error_flag = True
                    self.buffer = "Erro!"
            else:
                if self.error_flag:
                    self.error_flag = False
                    self.buffer = ""
                self.buffer += str(n)

        self.equation_display.set(str(self.buffer))

    def render_btns(self):
        n = 1

        for row in range(2, -1, -1): # sets the cursor to the 3rd row in the 1st column
            for column in range(3):

                btn = ctk.CTkButton(
                    master=self.btns_frame,
                    text=str(n),
                    width=self.BTN_SIZE,
                    height=self.BTN_SIZE,
                    corner_radius=18,
                    fg_color=self.NUMBER_BTN,
                    hover_color=self.NUMBER_HOVER,
                    font=(self.STD_FONT, 24, "bold"),
                    text_color="white",
                    command=lambda n=n: self.update_display(str(n))
                )

                btn.grid(row=row, column=column, padx=6, pady=6)

                n += 1

        zero_btn = ctk.CTkButton(
            master=self.btns_frame,
            text="0",
            width=self.BTN_SIZE,
            height=self.BTN_SIZE,
            corner_radius=18,
            fg_color=self.NUMBER_BTN,
            hover_color=self.NUMBER_HOVER,
            font=(self.STD_FONT, 24, "bold"),
            text_color="white",
            command=lambda n=n: self.update_display("0")
        )
        zero_btn.grid(row=3, column=1, padx=6, pady=6)

        dot_btn = ctk.CTkButton(
            master=self.btns_frame,
            text=".",
            width=self.BTN_SIZE,
            height=self.BTN_SIZE,
            corner_radius=18,
            fg_color=self.NUMBER_BTN,
            hover_color=self.NUMBER_HOVER,
            font=(self.STD_FONT, 24, "bold"),
            text_color="white",
            command=lambda n=".": self.update_display(n)
        )
        dot_btn.grid(row=3, column=2, padx=6, pady=6)

        clr_btn = ctk.CTkButton(
            master=self.btns_frame,
            text="C",
            width=self.BTN_SIZE,
            height=self.BTN_SIZE,
            corner_radius=18,
            fg_color="#D64545",
            hover_color="#EB5757",
            font=(self.STD_FONT, 24, "bold"),
            text_color="white",
            command=lambda n="C": self.update_display(n)
        )
        clr_btn.grid(row=3, column=0, padx=6, pady=6)


    def render_opr(self):
        operations = ['+', '-', 'x', '÷', '=']

        for row, opr in enumerate(operations):
            opr_btn = ctk.CTkButton(
                self.operations_frame,
                text=opr,
                width=self.BTN_SIZE,
                height=self.BTN_SIZE,
                corner_radius=18,
                fg_color=self.OP_BTN,
                hover_color=self.OP_HOVER,
                font=(self.STD_FONT, 24, "bold"),
                text_color="white",
                command=lambda opr=opr: self.update_display(f' {opr} ')
            )
            opr_btn.grid(column=0, row=row, padx=6, pady=6)


    def run(self):
        self.render_opr()
        self.render_btns()
        self.wdw.mainloop()


app = CalculatorApp()
app.run()