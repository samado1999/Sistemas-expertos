# Autor principal: ronak-07
# Adaptado por: Jorge E. Hernández
from experta import *
import tkinter as tk

diseases_list = []
diseases_symptoms = []
symptom_map = {}
d_desc_map = {}
d_treatment_map = {}

var1 = 0
var2 = 0
var3 = 0
var4 = 0
var5 = 0
var6 = 0
var7 = 0
var8 = 0
var9 = 0
var10 = 0
var11 = 0
var12 = 0
var13 = 0
var14 = 0
var15 = 0
var16 = 0
response = ''
app = ''


#
def preprocess():
    global diseases_list, diseases_symptoms, symptom_map, d_desc_map, d_treatment_map
    diseases = open("diseases.txt")
    diseases_t = diseases.read()
    diseases_list = diseases_t.split("\n")
    diseases.close()
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

    response = "The most probable disease that you have is %s\n" % id_disease + "\n" + "A short description of the " \
                                                                                       "disease is given below :\n" + \
               disease_details + "\n" + "The common medications and procedures suggested by other real doctors are: " \
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

    @Rule(Fact(action='find_disease'), NOT(Fact(headache=W())), salience=1)
    def symptom_0(self):
        # self.declare(Fact(headache=input("headache: ")))
        self.declare(Fact(headache=var1))

    @Rule(Fact(action='find_disease'), NOT(Fact(back_pain=W())), salience=1)
    def symptom_1(self):
        # self.declare(Fact(back_pain=input("back pain: ")))
        self.declare(Fact(back_pain=var2))

    @Rule(Fact(action='find_disease'), NOT(Fact(chest_pain=W())), salience=1)
    def symptom_2(self):
        # self.declare(Fact(chest_pain=input("chest pain: ")))
        self.declare(Fact(chest_pain=var3))

    @Rule(Fact(action='find_disease'), NOT(Fact(cough=W())), salience=1)
    def symptom_3(self):
        # self.declare(Fact(cough=input("cough: ")))
        self.declare(Fact(cough=var4))

    @Rule(Fact(action='find_disease'), NOT(Fact(fainting=W())), salience=1)
    def symptom_4(self):
        # self.declare(Fact(fainting=input("fainting: ")))
        self.declare(Fact(fainting=var5))

    @Rule(Fact(action='find_disease'), NOT(Fact(fatigue=W())), salience=1)
    def symptom_5(self):
        # self.declare(Fact(fatigue=input("fatigue: ")))
        self.declare(Fact(fatigue=var5))

    @Rule(Fact(action='find_disease'), NOT(Fact(sunken_eyes=W())), salience=1)
    def symptom_6(self):
        # self.declare(Fact(sunken_eyes=input("sunken eyes: ")))
        self.declare(Fact(sunken_eyes=var7))

    @Rule(Fact(action='find_disease'), NOT(Fact(low_body_temp=W())), salience=1)
    def symptom_7(self):
        # self.declare(Fact(low_body_temp=input("low body temperature: ")))
        self.declare(Fact(low_body_temp=var8))

    @Rule(Fact(action='find_disease'), NOT(Fact(restlessness=W())), salience=1)
    def symptom_8(self):
        # self.declare(Fact(restlessness=input("restlessness: ")))
        self.declare(Fact(restlessness=var9))

    @Rule(Fact(action='find_disease'), NOT(Fact(sore_throat=W())), salience=1)
    def symptom_9(self):
        # self.declare(Fact(sore_throat=input("sore throat: ")))
        self.declare(Fact(sore_throat=var10))

    @Rule(Fact(action='find_disease'), NOT(Fact(fever=W())), salience=1)
    def symptom_10(self):
        # self.declare(Fact(fever=input("fever: ")))
        self.declare(Fact(fever=var11))

    @Rule(Fact(action='find_disease'), NOT(Fact(nausea=W())), salience=1)
    def symptom_11(self):
        # self.declare(Fact(nausea=input("nausea: ")))
        self.declare(Fact(nausea=var12))

    @Rule(Fact(action='find_disease'), NOT(Fact(blurred_vision=W())), salience=1)
    def symptom_12(self):
        # self.declare(Fact(blurred_vision=input("blurred vision: ")))
        self.declare(Fact(blurred_vision=var13))

    @Rule(Fact(action='find_disease'), NOT(Fact(tiredness=W())), salience=1)
    def symptom_13(self):
        # self.declare(Fact(tiredness=input("tiredness: ")))
        self.declare(Fact(tiredness=var14))

    @Rule(Fact(action='find_disease'), NOT(Fact(smell=W())), salience=1)
    def symptom_14(self):
        # self.declare(Fact(smell=input("without smell: ")))
        self.declare(Fact(smell=var15))

    @Rule(Fact(action='find_disease'), NOT(Fact(taste=W())), salience=1)
    def symptom_15(self):
        # self.declare(Fact(taste=input("without taste: ")))
        self.declare(Fact(taste=var16))

    @Rule(Fact(action='find_disease'), Fact(headache="no"), Fact(back_pain="no"), Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="yes"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="yes"), Fact(sunken_eyes="no"), Fact(nausea="yes"),
          Fact(blurred_vision="no"), Fact(tiredness="no"), Fact(smell="no"), Fact(taste="no"))
    def disease_0(self):
        self.declare(Fact(disease="Jaundice"))

    @Rule(Fact(action='find_disease'), Fact(headache="no"), Fact(back_pain="no"), Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="no"), Fact(restlessness="yes"),
          Fact(low_body_temp="no"), Fact(fever="no"), Fact(sunken_eyes="no"), Fact(nausea="no"),
          Fact(blurred_vision="no"), Fact(tiredness="no"), Fact(smell="no"), Fact(taste="no"))
    def disease_1(self):
        self.declare(Fact(disease="Alzheimers"))

    @Rule(Fact(action='find_disease'), Fact(headache="no"), Fact(back_pain="yes"), Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="yes"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="no"), Fact(sunken_eyes="no"), Fact(nausea="no"),
          Fact(blurred_vision="no"), Fact(tiredness="no"), Fact(smell="no"), Fact(taste="no"))
    def disease_2(self):
        self.declare(Fact(disease="Arthritis"))

    @Rule(Fact(action='find_disease'), Fact(headache="no"), Fact(back_pain="no"), Fact(chest_pain="yes"),
          Fact(cough="yes"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="no"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="yes"), Fact(sunken_eyes="no"), Fact(nausea="no"),
          Fact(blurred_vision="no"), Fact(tiredness="no"), Fact(smell="no"), Fact(taste="no"))
    def disease_3(self):
        self.declare(Fact(disease="Tuberculosis"))

    @Rule(Fact(action='find_disease'), Fact(headache="no"), Fact(back_pain="no"), Fact(chest_pain="yes"),
          Fact(cough="yes"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="no"), Fact(restlessness="yes"),
          Fact(low_body_temp="no"), Fact(fever="no"), Fact(sunken_eyes="no"), Fact(nausea="no"),
          Fact(blurred_vision="no"), Fact(tiredness="no"), Fact(smell="no"), Fact(taste="no"))
    def disease_4(self):
        self.declare(Fact(disease="Asthma"))

    @Rule(Fact(action='find_disease'), Fact(headache="yes"), Fact(back_pain="no"), Fact(chest_pain="no"),
          Fact(cough="yes"), Fact(fainting="no"), Fact(sore_throat="yes"), Fact(fatigue="no"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="yes"), Fact(sunken_eyes="no"), Fact(nausea="no"),
          Fact(blurred_vision="no"), Fact(tiredness="no"), Fact(smell="no"), Fact(taste="no"))
    def disease_5(self):
        self.declare(Fact(disease="Sinusitis"))

    @Rule(Fact(action='find_disease'), Fact(headache="no"), Fact(back_pain="no"), Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="yes"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="no"), Fact(sunken_eyes="no"), Fact(nausea="no"),
          Fact(blurred_vision="no"), Fact(tiredness="no"), Fact(smell="no"), Fact(taste="no"))
    def disease_6(self):
        self.declare(Fact(disease="Epilepsy"))

    @Rule(Fact(action='find_disease'), Fact(headache="no"), Fact(back_pain="no"), Fact(chest_pain="yes"),
          Fact(cough="no"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="no"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="no"), Fact(sunken_eyes="no"), Fact(nausea="yes"),
          Fact(blurred_vision="no"), Fact(tiredness="no"), Fact(smell="no"), Fact(taste="no"))
    def disease_7(self):
        self.declare(Fact(disease="Heart Disease"))

    @Rule(Fact(action='find_disease'), Fact(headache="no"), Fact(back_pain="no"), Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="yes"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="no"), Fact(sunken_eyes="no"), Fact(nausea="yes"),
          Fact(blurred_vision="yes"), Fact(tiredness="no"), Fact(smell="no"), Fact(taste="no"))
    def disease_8(self):
        self.declare(Fact(disease="Diabetes"))

    @Rule(Fact(action='find_disease'), Fact(headache="yes"), Fact(back_pain="no"), Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="no"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="no"), Fact(sunken_eyes="no"), Fact(nausea="yes"),
          Fact(blurred_vision="yes"), Fact(tiredness="no"), Fact(smell="no"), Fact(taste="no"))
    def disease_9(self):
        self.declare(Fact(disease="Glaucoma"))

    @Rule(Fact(action='find_disease'), Fact(headache="no"), Fact(back_pain="no"), Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="yes"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="no"), Fact(sunken_eyes="no"), Fact(nausea="yes"),
          Fact(blurred_vision="no"), Fact(tiredness="no"), Fact(smell="no"), Fact(taste="no"))
    def disease_10(self):
        self.declare(Fact(disease="Hyperthyroidism"))

    @Rule(Fact(action='find_disease'), Fact(headache="yes"), Fact(back_pain="no"), Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fainting="no"), Fact(sore_throat="no"), Fact(fatigue="no"), Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="yes"), Fact(sunken_eyes="no"), Fact(nausea="yes"),
          Fact(blurred_vision="no"), Fact(tiredness="no"), Fact(smell="no"), Fact(taste="no"))
    def disease_11(self):
        self.declare(Fact(disease="Heat Stroke"))

    @Rule(Fact(action='find_disease'), Fact(headache="no"), Fact(back_pain="no"), Fact(chest_pain="no"),
          Fact(cough="no"), Fact(fainting="yes"), Fact(sore_throat="no"), Fact(fatigue="no"), Fact(restlessness="no"),
          Fact(low_body_temp="yes"), Fact(fever="no"), Fact(sunken_eyes="no"), Fact(nausea="no"),
          Fact(blurred_vision="no"), Fact(tiredness="no"), Fact(smell="no"), Fact(taste="no"))
    def disease_12(self):
        self.declare(Fact(disease="Hypothermia"))

    @Rule(Fact(action='find_disease'), Fact(headache="yes"), Fact(back_pain="no"), Fact(chest_pain="yes"),
          Fact(cough="no"), Fact(fainting="no"), Fact(sore_throat="yes"), Fact(fatigue="no"),
          Fact(restlessness="no"),
          Fact(low_body_temp="no"), Fact(fever="yes"), Fact(sunken_eyes="no"), Fact(nausea="no"),
          Fact(blurred_vision="no"), Fact(tiredness="yes"), Fact(smell="yes"), Fact(taste="yes"))
    def disease_13(self):
        self.declare(Fact(disease="Covid"))

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

        response = "The most probable disease that you have is %s\n" % id_disease + "\n" + "A short description of the " \
                                                                                           "disease is given below :\n" + \
                   disease_details + "\n" + "The common medications and procedures suggested by other real doctors " \
                                            "are: " \
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
          Fact(headache=MATCH.headache),
          Fact(back_pain=MATCH.back_pain),
          Fact(chest_pain=MATCH.chest_pain),
          Fact(cough=MATCH.cough),
          Fact(fainting=MATCH.fainting),
          Fact(sore_throat=MATCH.sore_throat),
          Fact(fatigue=MATCH.fatigue),
          Fact(low_body_temp=MATCH.low_body_temp),
          Fact(restlessness=MATCH.restlessness),
          Fact(fever=MATCH.fever),
          Fact(sunken_eyes=MATCH.sunken_eyes),
          Fact(nausea=MATCH.nausea),
          Fact(blurred_vision=MATCH.blurred_vision),
          Fact(tiredness=MATCH.tiredness),
          Fact(smell=MATCH.smell),
          Fact(taste=MATCH.taste), NOT(Fact(disease=MATCH.disease)), salience=-999)
    def not_matched(self, headache, back_pain, chest_pain, cough, fainting, sore_throat, fatigue, restlessness,
                    low_body_temp, fever, sunken_eyes, nausea, blurred_vision, tiredness, smell, taste):
        lis = [headache, back_pain, chest_pain, cough, fainting, sore_throat, fatigue, restlessness, low_body_temp,
               fever, sunken_eyes, nausea, blurred_vision, tiredness, smell, taste]
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

    w = tk.Label(app, text="Hi! I am Dr.Yar, I am here to help you make your health better. For that \n"
                           "you'll have to answer a few questions about your conditions. Do you feel \n"
                           "any of the following symptoms:")
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

    def print_selection():
        global var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12, var13, var14, var15, var16
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
        var15 = 'no'
        var16 = 'no'

        print(var14)
        print(var15)

        preprocess()
        engine = Greetings()
        engine.reset()  # Prepare the engine for the execution.
        engine.run()  # Run it!

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
