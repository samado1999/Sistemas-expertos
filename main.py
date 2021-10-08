# Autor principal: ronak-07
# Adaptado por: Jorge E. Hernández
from experta import *
import tkinter as tk

diseases_list = []
diseases_symptoms = []
symptom_map = {}
d_desc_map = {}
d_treatment_map = {}

def preprocess():
    global diseases_list, diseases_symptoms, symptom_map, d_desc_map, d_treatment_map
    diseases = open("diseases.txt")
    diseases_t = diseases.read()
    diseases_list = diseases_t.split("\n")
    diseases.close()
    print(diseases_list)
    for disease in diseases_list:
        disease_s_file = open("Disease symptoms/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        s_list = disease_s_data.split("\n")
        diseases_symptoms.append(s_list)
        symptom_map[str(s_list)] = disease
        disease_s_file.close()
        disease_s_file = open("Disease descriptions/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        d_desc_map[disease] = disease_s_data
        disease_s_file.close()
        disease_s_file = open("Disease treatments/" + disease + ".txt")
        disease_s_data = disease_s_file.read()
        d_treatment_map[disease] = disease_s_data
        disease_s_file.close()


'''
def identify_disease(*arguments):
    symptom_list = []
    for symptom in arguments:
        symptom_list.append(symptom)
    # Handle key error
    return symptom_map[str(symptom_list)]
'''


def get_details(disease):
    return d_desc_map[disease]


def get_treatments(disease):
    return d_treatment_map[disease]


def if_not_matched(disease):
    global response
    print("")
    id_disease = disease
    disease_details = get_details(id_disease)
    treatments = get_treatments(id_disease)
    print("")
    print("The most probable disease that you have is %s\n" % id_disease)
    print("A short description of the disease is given below :\n")
    print(disease_details + "\n")
    print("The common medications and procedures suggested by other real doctors are: \n")
    print(treatments + "\n")

    response = "La enfermedad más probable que tienes es %s\n" % id_disease + "\n" + "A continuación se ofrece una " \
                                                                                     "breve descripción de la " \
                                                                                     "enfermedad:\n" + \
               disease_details + "\n" + "Los medicamentos y procedimientos comunes sugeridos por otros médicos reales " \
                                        "son: " \
                                        "\n" + treatments + "\n "

    text2 = tk.Text(app, height=20, width=80)
    # scroll = tk.Scrollbar(app, command=text2.yview)
    # text2.configure(yscrollcommand=scroll.set)
    text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
    text2.tag_configure('big', font=('Verdana', 20, 'bold'))
    text2.tag_configure('color',
                        foreground='#476042',
                        font=('Tempus Sans ITC', 12, 'bold'))
    text2.insert(tk.END, response)

    text2.grid(column=2, row=1, sticky="E", padx=40, rowspan=13)


class Greetings(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        print("")
        print("Hi! I am Dr.Yar, I am here to help you make your health better.")
        print("For that you'll have to answer a few questions about your conditions")
        print("Do you feel any of the following symptoms:")
        print("")
        yield Fact(action="find_disease")

    @Rule(Fact(action='find_disease'), NOT(Fact(Fiebre=W())), salience=1)
    def symptom_0(self):
        # self.declare(Fact(Fiebre=input("Fiebre: ")))
        self.declare(Fact(Fiebre=var1))

    @Rule(Fact(action='find_disease'), NOT(Fact(Tos=W())), salience=1)
    def symptom_1(self):
        # self.declare(Fact(Tos=input("back pain: ")))
        self.declare(Fact(Tos=var2))

    @Rule(Fact(action='find_disease'), NOT(Fact(Moco=W())), salience=1)
    def symptom_2(self):
        # self.declare(Fact(Moco=input("chest pain: ")))
        self.declare(Fact(Moco=var3))

    @Rule(Fact(action='find_disease'), NOT(Fact(Congestion_nasal=W())), salience=1)
    def symptom_3(self):
        # self.declare(Fact(Congestion_nasal=input("Congestion_nasal: ")))
        self.declare(Fact(Congestion_nasal=var4))

    @Rule(Fact(action='find_disease'), NOT(Fact(Estornudos=W())), salience=1)
    def symptom_4(self):
        # self.declare(Fact(Estornudos=input("Estornudos: ")))
        self.declare(Fact(Estornudos=var5))

    @Rule(Fact(action='find_disease'), NOT(Fact(Dolor_garganta=W())), salience=1)
    def symptom_5(self):
        # self.declare(Fact(Malestar_garganta=input("Malestar_garganta: ")))
        self.declare(Fact(Dolor_garganta=var6))

    @Rule(Fact(action='find_disease'), NOT(Fact(Malestar_garganta=W())), salience=1)
    def symptom_6(self):
        # self.declare(Fact(Diarrea=input("sunken eyes: ")))
        self.declare(Fact(Malestar_garganta=var7))

    @Rule(Fact(action='find_disease'), NOT(Fact(Dificultad_respirar=W())), salience=1)
    def symptom_7(self):
        # self.declare(Fact(Dificultad_respirar=input("low body temperature: ")))
        self.declare(Fact(Dificultad_respirar=var8))

    @Rule(Fact(action='find_disease'), NOT(Fact(flema=W())), salience=1)
    def symptom_8(self):
        # self.declare(Fact(flema=input("flema: ")))
        self.declare(Fact(flema=var9))

    @Rule(Fact(action='find_disease'), NOT(Fact(Vomito=W())), salience=1)
    def symptom_9(self):
        # self.declare(Fact(Dolor_garganta=input("sore throat: ")))
        self.declare(Fact(Vomito=var10))

    @Rule(Fact(action='find_disease'), NOT(Fact(Diarrea=W())), salience=1)
    def symptom_10(self):
        # self.declare(Fact(Vomito=input("Vomito: ")))
        self.declare(Fact(Diarrea=var11))

    @Rule(Fact(action='find_disease'), NOT(Fact(Debilidad_Cansancio=W())), salience=1)
    def symptom_11(self):
        # self.declare(Fact(Debilidad_Cansancio=input("Debilidad_Cansancio: ")))
        self.declare(Fact(Debilidad_Cansancio=var12))

    @Rule(Fact(action='find_disease'), NOT(Fact(Dolor_huesos=W())), salience=1)
    def symptom_12(self):
        # self.declare(Fact(Dolor_huesos=input("blurred vision: ")))
        self.declare(Fact(Dolor_huesos=var13))

    @Rule(Fact(action='find_disease'), NOT(Fact(Radiografia_mancha=W())), salience=1)
    def symptom_13(self):
        # self.declare(Fact(Radiografia_mancha=input("Radiografia_mancha: ")))
        self.declare(Fact(Radiografia_mancha=var14))

    @Rule(Fact(action='find_disease'), AND(Fact(Fiebre="yes"), Fact(Tos="yes"), Fact(Moco="no"),
                                           Fact(Congestion_nasal="no"), Fact(Estornudos="no"),
                                           Fact(Dolor_garganta="yes"), Fact(Malestar_garganta="yes"), Fact(flema="yes"),
                                           Fact(Dificultad_respirar="yes"), Fact(Vomito="yes"), Fact(Diarrea="yes"),
                                           Fact(Debilidad_Cansancio="yes"),
                                           Fact(Dolor_huesos="no"), Fact(Radiografia_mancha="yes")))
    def disease_0(self):
        self.declare(Fact(disease="Covid-19"))

    @Rule(Fact(action='find_disease'), AND(Fact(Fiebre="yes"), Fact(Tos="yes"), Fact(Moco="yes"),
                                           Fact(Congestion_nasal="no"), Fact(Estornudos="yes"),
                                           Fact(Dolor_garganta="no"), Fact(Malestar_garganta="no"), Fact(flema="yes"),
                                           Fact(Dificultad_respirar="no"), Fact(Vomito="yes"), Fact(Diarrea="yes"),
                                           Fact(Debilidad_Cansancio="no"),
                                           Fact(Dolor_huesos="yes"), Fact(Radiografia_mancha="no")))
    def disease_1(self):
        self.declare(Fact(disease="Gripe"))

    @Rule(Fact(action='find_disease'), AND(Fact(Fiebre="no"), Fact(Tos="yes"), Fact(Moco="no"),
                                           Fact(Congestion_nasal="yes"), Fact(Estornudos="yes"),
                                           Fact(Dolor_garganta="no"), Fact(Malestar_garganta="no"), Fact(flema="yes"),
                                           Fact(Dificultad_respirar="no"), Fact(Vomito="no"), Fact(Diarrea="no"),
                                           Fact(Debilidad_Cansancio="no"),
                                           Fact(Dolor_huesos="no"), Fact(Radiografia_mancha="no")))
    def disease_2(self):
        self.declare(Fact(disease="Resfriado"))

    @Rule(Fact(action='find_disease'), AND(Fact(Fiebre="no"), Fact(Tos="no"), Fact(Moco="no"),
                                           Fact(Congestion_nasal="no"), Fact(Estornudos="no"),
                                           Fact(Dolor_garganta="no"), Fact(Malestar_garganta="no"), Fact(flema="no"),
                                           Fact(Dificultad_respirar="no"), Fact(Vomito="no"), Fact(Diarrea="no"),
                                           Fact(Debilidad_Cansancio="no"),
                                           Fact(Dolor_huesos="no"), Fact(Radiografia_mancha="no")))
    def disease_3(self):
        self.declare(Fact(disease="saludable"))

    @Rule(Fact(action='find_disease'), Fact(disease=MATCH.disease), salience=-998)
    def disease(self, disease):
        global response
        print("")
        id_disease = disease
        disease_details = get_details(id_disease)
        treatments = get_treatments(id_disease)
        print("")
        print("The most probable disease that you have is %s\n" % id_disease)
        print("A short description of the disease is given below :\n")
        print(disease_details + "\n")
        print("The common medications and procedures suggested by other real doctors are: \n")
        print(treatments + "\n")

        response = "La enfermedad más probable que tienes es %s\n" % id_disease + "\n" + "A continuación se ofrece una " \
                                                                                         "breve descripción de la " \
                                                                                         "enfermedad:\n" + \
                   disease_details + "\n" + "Los medicamentos y procedimientos comunes sugeridos por otros médicos " \
                                            "reales " \
                                            "son: " \
                                            "\n" + treatments + "\n "

        text2 = tk.Text(app, height=20, width=80)
        # scroll = tk.Scrollbar(app, command=text2.yview)
        # text2.configure(yscrollcommand=scroll.set)
        text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
        text2.tag_configure('big', font=('Verdana', 20, 'bold'))
        text2.tag_configure('color',
                            foreground='#476042',
                            font=('Tempus Sans ITC', 12, 'bold'))
        text2.insert(tk.END, response)

        text2.grid(column=2, row=1, sticky="E", padx=40, rowspan=13)

    @Rule(Fact(action='find_disease'),
          Fact(Fiebre=MATCH.Fiebre),
          Fact(Tos=MATCH.Tos),
          Fact(Moco=MATCH.Moco),
          Fact(Congestion_nasal=MATCH.Congestion_nasal),
          Fact(Estornudos=MATCH.Estornudos),
          Fact(Dolor_garganta=MATCH.Dolor_garganta),
          Fact(Malestar_garganta=MATCH.Malestar_garganta),
          Fact(Dificultad_respirar=MATCH.Dificultad_respirar),
          Fact(flema=MATCH.flema),
          Fact(Vomito=MATCH.Vomito),
          Fact(Diarrea=MATCH.Diarrea),
          Fact(Debilidad_Cansancio=MATCH.Debilidad_Cansancio),
          Fact(Dolor_huesos=MATCH.Dolor_huesos),
          Fact(Radiografia_mancha=MATCH.Radiografia_mancha), NOT(Fact(disease=MATCH.disease)), salience=-999)
    def not_matched(self, Fiebre, Tos, Moco, Congestion_nasal, Estornudos, Dolor_garganta, Malestar_garganta, flema,
                    Dificultad_respirar, Vomito, Diarrea, Debilidad_Cansancio, Dolor_huesos, Radiografia_mancha):
        lis = [Fiebre, Tos, Moco, Congestion_nasal, Estornudos, Dolor_garganta, Malestar_garganta, flema,
               Dificultad_respirar,
               Vomito, Diarrea, Debilidad_Cansancio, Dolor_huesos, Radiografia_mancha]
        max_count = 0
        max_disease = ""
        for key, val in symptom_map.items():
            count = 0
            temp_list = eval(key)
            for j in range(0, len(lis)):
                if temp_list[j] == lis[j] and lis[j] == "yes":
                    count = count + 1
            if count > max_count:
                max_count = count
                max_disease = val
        if_not_matched(max_disease)

# Creación de la interfaz gráfica
# Se tienen en cuenta 2 valores para cada síntoma: 1 cuando si sufre del sintoma y 0 en caso contrario
def make_interface():
    global app

    app = tk.Tk()
    app.geometry('1000x450')
    app.resizable(False, False)

    var1c = tk.IntVar()
    cFiebre = tk.Checkbutton(app, text='Fiebre', variable=var1c, onvalue=1, offvalue=0)
    var2c = tk.IntVar()
    cTos = tk.Checkbutton(app, text='Tos', variable=var2c, onvalue=1, offvalue=0)
    var3c = tk.IntVar()
    cMoco = tk.Checkbutton(app, text='Moco', variable=var3c, onvalue=1, offvalue=0)
    var4c = tk.IntVar()
    cCongestion = tk.Checkbutton(app, text='Congestión nasal', variable=var4c, onvalue=1, offvalue=0)
    var5c = tk.IntVar()
    cEstornudo = tk.Checkbutton(app, text='Estornudos', variable=var5c, onvalue=1, offvalue=0)
    var6c = tk.IntVar()
    cDolorGarganta = tk.Checkbutton(app, text='Dolor de garganta', variable=var6c, onvalue=1, offvalue=0)
    var7c = tk.IntVar()
    cMalestarGarganta = tk.Checkbutton(app, text='Malestar en la garganta', variable=var7c, onvalue=1, offvalue=0)
    var8c = tk.IntVar()
    cRespirar = tk.Checkbutton(app, text='Dificultad para respirar', variable=var8c, onvalue=1, offvalue=0)
    var9c = tk.IntVar()
    cFlema = tk.Checkbutton(app, text='flema', variable=var9c, onvalue=1, offvalue=0)
    var10c = tk.IntVar()
    cVomito = tk.Checkbutton(app, text='Vómito', variable=var10c, onvalue=1, offvalue=0)
    var11c = tk.IntVar()
    cDiarrea = tk.Checkbutton(app, text='Diarrea', variable=var11c, onvalue=1, offvalue=0)
    var12c = tk.IntVar()
    cDebilidad = tk.Checkbutton(app, text='Debilidad o Cansancio', variable=var12c, onvalue=1, offvalue=0)
    var13c = tk.IntVar()
    cHuesos = tk.Checkbutton(app, text='Dolor en los huesos', variable=var13c, onvalue=1, offvalue=0)
    var14c = tk.IntVar()
    cPulmon = tk.Checkbutton(app, text='Radiografíadel pulmón con mancha', variable=var14c, onvalue=1, offvalue=0)

    cFiebre.grid(column=0, row=1, sticky="W")
    cTos.grid(column=0, row=2, sticky="W")
    cMoco.grid(column=0, row=3, sticky="W")
    cCongestion.grid(column=0, row=4, sticky="W")
    cEstornudo.grid(column=0, row=5, sticky="W")
    cDolorGarganta.grid(column=0, row=6, sticky="W")
    cMalestarGarganta.grid(column=0, row=7, sticky="W")
    cRespirar.grid(column=0, row=8, sticky="W")
    cFlema.grid(column=0, row=9, sticky="W")
    cVomito.grid(column=0, row=10, sticky="W")
    cDiarrea.grid(column=0, row=11, sticky="W")
    cDebilidad.grid(column=0, row=12, sticky="W")
    cHuesos.grid(column=0, row=13, sticky="W")
    cPulmon.grid(column=0, row=14, sticky="W")

    # labelValue = tk.Label(app, textvariable=radioValue)
    # labelValue.grid(column=2, row=0, sticky="E", padx=40)

    w = tk.Label(app, text="¡Hola! Soy el Dr. Yar, estoy aquí para ayudarlo a mejorar su salud. Para \n"
                           "eso tendrás que responder algunas preguntas sobre tus condiciones. \n"
                           "¿Siente alguno de los siguientes síntomas?:")
    w.grid(column=2, row=0, sticky="E", padx=40)

    text2 = tk.Text(app, height=20, width=80)
    # scroll = tk.Scrollbar(app, command=text2.yview)
    # text2.configure(yscrollcommand=scroll.set)
    text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
    text2.tag_configure('big', font=('Verdana', 20, 'bold'))
    text2.tag_configure('color',
                        foreground='#476042',
                        font=('Tempus Sans ITC', 12, 'bold'))

    text2.insert(tk.END, '')

    text2.grid(column=2, row=1, sticky="E", padx=40, rowspan=13)

    # Aquí asocio los valores de los checkboxes (1 y 0) con respuestas que el sistema experto pueda procesar para el diagnóstico (yes, no)
    def print_selection():
        global var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12, var13, var14
        var1 = 'no' if var1c.get() == 0 else 'yes'
        var2 = 'no' if var2c.get() == 0 else 'yes'
        var3 = 'no' if var3c.get() == 0 else 'yes'
        var4 = 'no' if var4c.get() == 0 else 'yes'
        var5 = 'no' if var5c.get() == 0 else 'yes'
        var6 = 'no' if var6c.get() == 0 else 'yes'
        var7 = 'no' if var7c.get() == 0 else 'yes'
        var8 = 'no' if var8c.get() == 0 else 'yes'
        var9 = 'no' if var9c.get() == 0 else 'yes'
        var10 = 'no' if var10c.get() == 0 else 'yes'
        var11 = 'no' if var11c.get() == 0 else 'yes'
        var12 = 'no' if var12c.get() == 0 else 'yes'
        var13 = 'no' if var13c.get() == 0 else 'yes'
        var14 = 'no' if var14c.get() == 0 else 'yes'
        print(var14)

        preprocess()
        engine = Greetings()
        engine.reset()  # Prepare the engine for the execution.
        engine.run()  # Run it!
    # Creación del botón que lanzará el diagnóstico en el textbox
    msbtn = tk.Button(app, text='DIAGNOSTICAR',
                      command=lambda: print_selection())
    msbtn.grid(column=2, row=15, sticky="E", padx=40)

    app.mainloop()


if __name__ == "__main__":
    '''
    preprocess()
    engine = Greetings()
    while 1:
        engine.reset()  # Prepare the engine for the execution.
        engine.run()  # Run it!
        print("Would you like to diagnose some other symptoms?")
        if input() == "no":
            exit()
    '''
    make_interface()
