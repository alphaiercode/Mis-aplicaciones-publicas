import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMessageBox, QDialog, QTableWidgetItem, QVBoxLayout, QLabel
from PyQt5 import uic
from PyQt5.QtGui import QIcon, QPixmap
import pyttsx3


class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("principal.ui", self)

        self.btn_pronunciar.clicked.connect(self.Pronunciar)
        self.btn_gato.clicked.connect(self.Gato)
        self.btn_perro.clicked.connect(self.Perro)
        self.btn_oso.clicked.connect(self.Oso)
        self.btn_caballo.clicked.connect(self.Caballo)
        self.btn_leon.clicked.connect(self.Leon)
        self.btn_vaca.clicked.connect(self.Vaca)
        self.btn_pajaro.clicked.connect(self.Pajaro)
        self.btn_conejo.clicked.connect(self.Conejo)
        self.btn_raton.clicked.connect(self.Raton)

        self.btn_auto.clicked.connect(self.Auto)
        self.btn_moto.clicked.connect(self.Moto)
        self.btn_bici.clicked.connect(self.Bici)
        self.btn_camion.clicked.connect(self.Camion)
        self.btn_avion.clicked.connect(self.Avion)
        self.btn_helicoptero.clicked.connect(self.Helicoptero)

        self.btn_lentes.clicked.connect(self.Lentes)
        self.btn_celular.clicked.connect(self.Celular)
        self.btn_cama.clicked.connect(self.Cama)
        self.btn_mochila.clicked.connect(self.Mochila)
        self.btn_mate.clicked.connect(self.Mate)
        self.btn_mesa.clicked.connect(self.Mesa)
        self.btn_silla.clicked.connect(self.Silla)
        self.btn_tv.clicked.connect(self.Television)
        self.btn_puerta.clicked.connect(self.Puerta)

        self.btn_banana.clicked.connect(self.Banana)
        self.btn_mandarina.clicked.connect(self.Mandarina)
        self.btn_manzana.clicked.connect(self.Manzana)
        self.btn_pera.clicked.connect(self.Pera)
        self.btn_sandia.clicked.connect(self.Sandia)
        self.btn_uva.clicked.connect(self.Uva)
        self.btn_naranja.clicked.connect(self.Naranja)
        self.btn_pomelo.clicked.connect(self.Pomelo)
        self.btn_kiwi.clicked.connect(self.Kiwi)

        self.btn_sopa.clicked.connect(self.Sopa)
        self.btn_carne.clicked.connect(self.Carne)
        self.btn_milanesa.clicked.connect(self.Milanesa)
        self.btn_fideos.clicked.connect(self.Fideos)
        self.btn_pure.clicked.connect(self.Pure)
        self.btn_ensalada.clicked.connect(self.Ensalada)

        self.btn_1.clicked.connect(self.Num1)
        self.btn_2.clicked.connect(self.Num2)
        self.btn_3.clicked.connect(self.Num3)
        self.btn_4.clicked.connect(self.Num4)
        self.btn_5.clicked.connect(self.Num5)
        self.btn_6.clicked.connect(self.Num6)
        self.btn_7.clicked.connect(self.Num7)
        self.btn_8.clicked.connect(self.Num8)
        self.btn_9.clicked.connect(self.Num9)
        self.btn_10.clicked.connect(self.Num10)

        self.btn_a.clicked.connect(self.letra_a)
        self.btn_b.clicked.connect(self.letra_b)
        self.btn_c.clicked.connect(self.letra_c)
        self.btn_d.clicked.connect(self.letra_d)
        self.btn_e.clicked.connect(self.letra_e)
        self.btn_f.clicked.connect(self.letra_f)
        self.btn_g.clicked.connect(self.letra_g)
        self.btn_h.clicked.connect(self.letra_h)
        self.btn_i.clicked.connect(self.letra_i)
        self.btn_j.clicked.connect(self.letra_j)
        self.btn_k.clicked.connect(self.letra_k)
        self.btn_l.clicked.connect(self.letra_l)
        self.btn_m.clicked.connect(self.letra_m)
        self.btn_n.clicked.connect(self.letra_n)
        self.btn_o.clicked.connect(self.letra_o)
        self.btn_p.clicked.connect(self.letra_p)
        self.btn_q.clicked.connect(self.letra_q)
        self.btn_r.clicked.connect(self.letra_r)
        self.btn_s.clicked.connect(self.letra_s)
        self.btn_t.clicked.connect(self.letra_t)
        self.btn_u.clicked.connect(self.letra_u)
        self.btn_v.clicked.connect(self.letra_v)
        self.btn_w.clicked.connect(self.letra_w)
        self.btn_x.clicked.connect(self.letra_x)
        self.btn_y.clicked.connect(self.letra_y)
        self.btn_z.clicked.connect(self.letra_z)

        self.btn_salir.clicked.connect(self.Salir)
        self.info.triggered.connect(self.Informacion)

    def Informacion(self):
        QMessageBox.information(self, "Informacion", "Desarrolado por Alphaier - kdpasquariello@gmail.com")


    def Salir(self):
        quit()


    def Pronunciar(self):
        engine = pyttsx3.init()
        engine.setProperty('rate', 120)

        voices = engine.getProperty('voices')
        #indice para voz [0] - Español-HELENA

        engine.setProperty('voice', voices[0].id)

        engine.say(self.caja_titulo.text())
        engine.runAndWait()

    def Gato(self):
        self.caja_titulo.setText("Gato")
        pixmap = QPixmap("Elementos/gato.jpg")
        self.foto.setPixmap(pixmap)

    def Perro(self):
        self.caja_titulo.setText("Perro")
        pixmap = QPixmap("Elementos/perro.jpg")
        self.foto.setPixmap(pixmap)

    def Oso(self):
        self.caja_titulo.setText("Oso")
        pixmap = QPixmap("Elementos/oso.jpg")
        self.foto.setPixmap(pixmap)

    def Caballo(self):
        self.caja_titulo.setText("Caballo")
        pixmap = QPixmap("Elementos/caballo.jpg")
        self.foto.setPixmap(pixmap)

    def Leon(self):
        self.caja_titulo.setText("Leon")
        pixmap = QPixmap("Elementos/leon.jpg")
        self.foto.setPixmap(pixmap)

    def Vaca(self):
        self.caja_titulo.setText("Vaca")
        pixmap = QPixmap("Elementos/vaca.jpg")
        self.foto.setPixmap(pixmap)

    def Pajaro(self):
        self.caja_titulo.setText("Pajaro")
        pixmap = QPixmap("Elementos/pajaro.jpg")
        self.foto.setPixmap(pixmap)

    def Conejo(self):
        self.caja_titulo.setText("Conejo")
        pixmap = QPixmap("Elementos/conejo.jpg")
        self.foto.setPixmap(pixmap)

    def Raton(self):
        self.caja_titulo.setText("Raton")
        pixmap = QPixmap("Elementos/rata.jpg")
        self.foto.setPixmap(pixmap)

    def Auto(self):
        self.caja_titulo.setText("Automovil")
        pixmap = QPixmap("Elementos/auto.jpg")
        self.foto.setPixmap(pixmap)

    def Moto(self):
        self.caja_titulo.setText("Motocicleta")
        pixmap = QPixmap("Elementos/moto.jpg")
        self.foto.setPixmap(pixmap)

    def Bici(self):
        self.caja_titulo.setText("Bicicleta")
        pixmap = QPixmap("Elementos/bicicleta.jpg")
        self.foto.setPixmap(pixmap)

    def Camion(self):
        self.caja_titulo.setText("Camion")
        pixmap = QPixmap("Elementos/camion.jpg")
        self.foto.setPixmap(pixmap)

    def Avion(self):
        self.caja_titulo.setText("Avion")
        pixmap = QPixmap("Elementos/avion.jpg")
        self.foto.setPixmap(pixmap)

    def Helicoptero(self):
        self.caja_titulo.setText("Helicoptero")
        pixmap = QPixmap("Elementos/helicoptero.jpg")
        self.foto.setPixmap(pixmap)

    def Lentes(self):
        self.caja_titulo.setText("Anteojos")
        pixmap = QPixmap("Elementos/anteojos.jpg")
        self.foto.setPixmap(pixmap)

    def Celular(self):
        self.caja_titulo.setText("Celular")
        pixmap = QPixmap("Elementos/celular.jpg")
        self.foto.setPixmap(pixmap)

    def Cama(self):
        self.caja_titulo.setText("Cama")
        pixmap = QPixmap("Elementos/cama.jpg")
        self.foto.setPixmap(pixmap)

    def Mochila(self):
        self.caja_titulo.setText("Mochila")
        pixmap = QPixmap("Elementos/mochila.jpg")
        self.foto.setPixmap(pixmap)

    def Mate(self):
        self.caja_titulo.setText("Mate")
        pixmap = QPixmap("Elementos/mate.jpg")
        self.foto.setPixmap(pixmap)

    def Mesa(self):
        self.caja_titulo.setText("Mesa")
        pixmap = QPixmap("Elementos/mesa.jpg")
        self.foto.setPixmap(pixmap)

    def Silla(self):
        self.caja_titulo.setText("Silla")
        pixmap = QPixmap("Elementos/silla.jpg")
        self.foto.setPixmap(pixmap)

    def Television(self):
        self.caja_titulo.setText("Television")
        pixmap = QPixmap("Elementos/tele.jpg")
        self.foto.setPixmap(pixmap)

    def Puerta(self):
        self.caja_titulo.setText("Puerta")
        pixmap = QPixmap("Elementos/puerta.jpg")
        self.foto.setPixmap(pixmap)

    def Banana(self):
        self.caja_titulo.setText("Banana")
        pixmap = QPixmap("Elementos/banana.jpg")
        self.foto.setPixmap(pixmap)

    def Mandarina(self):
        self.caja_titulo.setText("Mandarina")
        pixmap = QPixmap("Elementos/mandarina.jpg")
        self.foto.setPixmap(pixmap)

    def Manzana(self):
        self.caja_titulo.setText("Manzana")
        pixmap = QPixmap("Elementos/manzana.jpg")
        self.foto.setPixmap(pixmap)

    def Pera(self):
        self.caja_titulo.setText("Pera")
        pixmap = QPixmap("Elementos/pera.jpg")
        self.foto.setPixmap(pixmap)

    def Sandia(self):
        self.caja_titulo.setText("Sandia")
        pixmap = QPixmap("Elementos/sandia.jpg")
        self.foto.setPixmap(pixmap)

    def Uva(self):
        self.caja_titulo.setText("Uvas")
        pixmap = QPixmap("Elementos/uva.jpg")
        self.foto.setPixmap(pixmap)

    def Naranja(self):
        self.caja_titulo.setText("Naranja")
        pixmap = QPixmap("Elementos/naranja.jpg")
        self.foto.setPixmap(pixmap)

    def Pomelo(self):
        self.caja_titulo.setText("Pomelo")
        pixmap = QPixmap("Elementos/pomelo.jpg")
        self.foto.setPixmap(pixmap)

    def Kiwi(self):
        self.caja_titulo.setText("Kiwi")
        pixmap = QPixmap("Elementos/kiwi.jpg")
        self.foto.setPixmap(pixmap)

    def Sopa(self):
        self.caja_titulo.setText("Sopa")
        pixmap = QPixmap("Elementos/sopa.jpg")
        self.foto.setPixmap(pixmap)

    def Carne(self):
        self.caja_titulo.setText("Carne")
        pixmap = QPixmap("Elementos/carne.jpg")
        self.foto.setPixmap(pixmap)

    def Milanesa(self):
        self.caja_titulo.setText("Milanesa")
        pixmap = QPixmap("Elementos/milanesa.jpg")
        self.foto.setPixmap(pixmap)

    def Fideos(self):
        self.caja_titulo.setText("Fideos")
        pixmap = QPixmap("Elementos/fideos.jpg")
        self.foto.setPixmap(pixmap)

    def Pure(self):
        self.caja_titulo.setText("Pure")
        pixmap = QPixmap("Elementos/pure.jpg")
        self.foto.setPixmap(pixmap)

    def Ensalada(self):
        self.caja_titulo.setText("Ensalada")
        pixmap = QPixmap("Elementos/ensalada.jpg")
        self.foto.setPixmap(pixmap)

    def Num1(self):
        self.caja_titulo.setText("1")
        pixmap = QPixmap("Numeros/1.png")
        self.foto.setPixmap(pixmap)

    def Num2(self):
        self.caja_titulo.setText("2")
        pixmap = QPixmap("Numeros/2.png")
        self.foto.setPixmap(pixmap)

    def Num3(self):
        self.caja_titulo.setText("3")
        pixmap = QPixmap("Numeros/3.png")
        self.foto.setPixmap(pixmap)

    def Num4(self):
        self.caja_titulo.setText("4")
        pixmap = QPixmap("Numeros/4.jpg")
        self.foto.setPixmap(pixmap)

    def Num5(self):
        self.caja_titulo.setText("5")
        pixmap = QPixmap("Numeros/5.jpg")
        self.foto.setPixmap(pixmap)

    def Num6(self):
        self.caja_titulo.setText("6")
        pixmap = QPixmap("Numeros/6.png")
        self.foto.setPixmap(pixmap)

    def Num7(self):
        self.caja_titulo.setText("7")
        pixmap = QPixmap("Numeros/7.jpg")
        self.foto.setPixmap(pixmap)

    def Num8(self):
        self.caja_titulo.setText("8")
        pixmap = QPixmap("Numeros/8.jpg")
        self.foto.setPixmap(pixmap)

    def Num9(self):
        self.caja_titulo.setText("9")
        pixmap = QPixmap("Numeros/9.jpg")
        self.foto.setPixmap(pixmap)

    def Num10(self):
        self.caja_titulo.setText("10")
        pixmap = QPixmap("Numeros/10.jpg")
        self.foto.setPixmap(pixmap)

    def letra_a(self):
        self.caja_titulo.setText("A")
        pixmap = QPixmap("Letras/a.jpg")
        self.foto.setPixmap(pixmap)

    def letra_b(self):
        self.caja_titulo.setText("B")
        pixmap = QPixmap("Letras/b.jpg")
        self.foto.setPixmap(pixmap)

    def letra_c(self):
        self.caja_titulo.setText("C")
        pixmap = QPixmap("Letras/c.jpg")
        self.foto.setPixmap(pixmap)

    def letra_d(self):
        self.caja_titulo.setText("D")
        pixmap = QPixmap("Letras/d.jpg")
        self.foto.setPixmap(pixmap)

    def letra_e(self):
        self.caja_titulo.setText("E")
        pixmap = QPixmap("Letras/e.jpg")
        self.foto.setPixmap(pixmap)

    def letra_f(self):
        self.caja_titulo.setText("F")
        pixmap = QPixmap("Letras/f.jpg")
        self.foto.setPixmap(pixmap)

    def letra_g(self):
        self.caja_titulo.setText("G")
        pixmap = QPixmap("Letras/g.jpg")
        self.foto.setPixmap(pixmap)

    def letra_h(self):
        self.caja_titulo.setText("H")
        pixmap = QPixmap("Letras/h.jpg")
        self.foto.setPixmap(pixmap)

    def letra_i(self):
        self.caja_titulo.setText("I")
        pixmap = QPixmap("Letras/i.jpg")
        self.foto.setPixmap(pixmap)

    def letra_j(self):
        self.caja_titulo.setText("J")
        pixmap = QPixmap("Letras/j.jpg")
        self.foto.setPixmap(pixmap)

    def letra_k(self):
        self.caja_titulo.setText("K")
        pixmap = QPixmap("Letras/k.jpg")
        self.foto.setPixmap(pixmap)

    def letra_l(self):
        self.caja_titulo.setText("L")
        pixmap = QPixmap("Letras/l.jpg")
        self.foto.setPixmap(pixmap)

    def letra_m(self):
        self.caja_titulo.setText("M")
        pixmap = QPixmap("Letras/m.jpg")
        self.foto.setPixmap(pixmap)

    def letra_n(self):
        self.caja_titulo.setText("N")
        pixmap = QPixmap("Letras/n.jpg")
        self.foto.setPixmap(pixmap)

    def letra_o(self):
        self.caja_titulo.setText("O")
        pixmap = QPixmap("Letras/o.jpg")
        self.foto.setPixmap(pixmap)

    def letra_p(self):
        self.caja_titulo.setText("P")
        pixmap = QPixmap("Letras/p.jpg")
        self.foto.setPixmap(pixmap)

    def letra_q(self):
        self.caja_titulo.setText("Q")
        pixmap = QPixmap("Letras/q.jpg")
        self.foto.setPixmap(pixmap)

    def letra_r(self):
        self.caja_titulo.setText("R")
        pixmap = QPixmap("Letras/r.jpg")
        self.foto.setPixmap(pixmap)

    def letra_s(self):
        self.caja_titulo.setText("S")
        pixmap = QPixmap("Letras/s.jpg")
        self.foto.setPixmap(pixmap)

    def letra_t(self):
        self.caja_titulo.setText("T")
        pixmap = QPixmap("Letras/t.jpg")
        self.foto.setPixmap(pixmap)

    def letra_u(self):
        self.caja_titulo.setText("U")
        pixmap = QPixmap("Letras/u.jpg")
        self.foto.setPixmap(pixmap)

    def letra_v(self):
        self.caja_titulo.setText("V")
        pixmap = QPixmap("Letras/v.jpg")
        self.foto.setPixmap(pixmap)

    def letra_w(self):
        self.caja_titulo.setText("W")
        pixmap = QPixmap("Letras/w.jpg")
        self.foto.setPixmap(pixmap)

    def letra_x(self):
        self.caja_titulo.setText("X")
        pixmap = QPixmap("Letras/x.jpg")
        self.foto.setPixmap(pixmap)

    def letra_y(self):
        self.caja_titulo.setText("Y")
        pixmap = QPixmap("Letras/y.jpg")
        self.foto.setPixmap(pixmap)

    def letra_z(self):
        self.caja_titulo.setText("Z")
        pixmap = QPixmap("Letras/z.jpg")
        self.foto.setPixmap(pixmap)




app = QApplication(sys.argv)
window = Window()
window.show()
app.exec_()
