#!/usr/bin/env python3
import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMessageBox, QDialog, QTableWidgetItem, QVBoxLayout, QLabel
from PyQt5 import uic
from PyQt5.QtGui import QIcon, QPixmap


class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("principal.ui", self)

        img_default = QPixmap("musculos/lupa.png")
        self.btn_bicep.clicked.connect(self.bicep_click)
        self.btn_deltoides.clicked.connect(self.deltoides_click)
        self.btn_pectoral.clicked.connect(self.pectoral_click)
        self.btn_serrato.clicked.connect(self.serrato_click)
        self.btn_flexor.clicked.connect(self.flexor_click)
        self.btn_cuadriceps.clicked.connect(self.cuadriceps_click)
        self.btn_tibial.clicked.connect(self.tibial_click)
        self.btn_soleo.clicked.connect(self.soleo_click)
        self.btn_gemelos.clicked.connect(self.gemelos_click)
        self.btn_vasto_interno.clicked.connect(self.vasto_interno_click)
        self.btn_vasto_externo.clicked.connect(self.vasto_externo_click)
        self.btn_recto.clicked.connect(self.recto_click)
        self.btn_supinador.clicked.connect(self.supinador_click)
        self.btn_cuello.clicked.connect(self.cuello_click)
        self.btn_frontal.clicked.connect(self.frontal_click)

    def bicep_click(self):
        self.caja_titulo.setText("Biceps")
        self.caja_informacion.clear()
        self.caja_informacion.insertPlainText("El músculo bíceps braquial se encuentra en el brazo, cubriendo los músculos braquial anterior y coracobraquial. En su sector superior presenta una porción larga (que desciende por el húmero) y una porción corta (originada por un tendón que comparte con el músculo coracobraquial).")

        pixmap = QPixmap("musculos/Biceps.jpg")
        self.foto.setPixmap(pixmap)

    def deltoides_click(self):
        self.caja_titulo.setText("Deltoides")
        self.caja_informacion.clear()
        self.caja_informacion.insertPlainText("Músculo deltoides. El músculo deltoides cubre la extremidad proximal del húmero. Tiene forma triangular y se inicia en el tercio lateral de la clavícula, en el acromion y en la espina de la escápula en toda su extensión. Los fascículos anteriores y posteriores del músculo se dirigen casi en línea recta hacia abajo y lateralmente; los fascículos medios, flexionándose a través de la cabeza del húmero, se dirigen directamente hacia abaja. Todos los fascículos convergen, insertándose en la tuberosidad deltoidea, que tiene el húmero en su parte media. Entre la cara interna del músculo y la cabeza del húmero se encuentra la bolsa sinovial subdeltoidea. ")

        pixmap = QPixmap("musculos/deltoides.jpg")
        self.foto.setPixmap(pixmap)

    def pectoral_click(self):
        self.caja_titulo.setText("Pectoral Mayor")
        self.caja_informacion.clear()
        self.caja_informacion.insertPlainText("El músculo pectoral mayor es un músculo superficial, plano, ubicado en la región anterosuperior del tórax. Se origina en la mitad medial del borde anterior de la clavícula, cara anterior del esternón, 6 primeros cartílagos costales y aponeurosis del oblicuo externo, para luego insertarse en el labio externo o lateral de la corredera bicipital (también conocida como surco intertubercular) hueso del humero. Está inervado por los nervios pectorales medial y lateral, que tienen origen en el plexo braquial. La piel que recubre este músculo está inervada por T2 a T6. ")

        pixmap = QPixmap("musculos/pectoral.jpg")
        self.foto.setPixmap(pixmap)

    def serrato_click(self):
        self.caja_titulo.setText("Serrato anterior")
        self.caja_informacion.clear()
        self.caja_informacion.insertPlainText("Su principal función es la de estabilizar la escápula. Su tono basal garantiza la correcta aplicación de la escápula al tórax y evita que el borde medial de la escápula se separe en sentido posterior. Si falla el músculo por debilidad o parálisis se observa el signo de escápula alada. Su parte superior eleva la escápula, su parte media desciende la misma así como su parte inferior desciende la escápula y gira su ángulo inferior externamente para permitir la elevación del brazo más allá de la horizontal juntamente con el músculo trapecio. En el tórax con la escápula como punto fijo, eleva las costillas (inspiración). Su función en cadena cinética abierta es la abducción escapular (rotación con el vértice inferior hacia lateral) y aducción escapular, y en cadena cinética cerrada es la anteriorización del tórax respecto al brazo y a la misma escápula.")

        pixmap = QPixmap("musculos/serrato.jpg")
        self.foto.setPixmap(pixmap)

    def flexor_click(self):
        self.caja_titulo.setText("Flexor del antebrazo")
        self.caja_informacion.clear()
        self.caja_informacion.insertPlainText("El músculo flexor radial del carpo o palmar mayor es un músculo del antebrazo situado por dentro del pronador redondo y que junto a él y al palmar menor y el cubital anterior forman el primer plano o plano superficial del grupo de músculos anteriores del antebrazo. Por su origen común, estos cuatro músculos también reciben el nombre de epitrocleares. Se origina en la epitróclea. Desde ahí se dirige hacia abajo y hacia afuera para continuarse con un tendón en el tercio inferior del antebrazo hasta insertarse en la cara anterior del extremo superior del segundo metacarpiano. Su acción es de flexor principal de la muñeca, con tendencia a su abducción y pronación. También es flexor del codo. Inervado por el nervio mediano. Vascularizado por ramas de las arterias cubital y radial. ")

        pixmap = QPixmap("musculos/flexor.png")
        self.foto.setPixmap(pixmap)

    def cuadriceps_click(self):
        self.caja_titulo.setText("Cuadriceps")
        self.caja_informacion.clear()
        self.caja_informacion.insertPlainText("El músculo cuádriceps femoral es el músculo más voluminoso de todo el cuerpo humano. Es el que soporta nuestro peso y nos permite andar, caminar, sentarnos y correr. Se denomina cuádriceps debido a que tiene cuatro cabezas musculares. Se encuentra en la cara anterior del fémur. Los cuádriceps son potentes extensores de la articulación de la rodilla. Son cruciales para caminar, correr, saltar y ponerse en cuclillas. Debido a que el recto femoral se conecta al hueso ilion, también es un flexor de la cadera. Esta acción también es crucial para caminar o correr, ya que balancea la pierna hacia adelante en el siguiente paso. Los cuádriceps, específicamente el vasto medial, desempeñan la importante función de estabilización de la rótula y la articulación de la rodilla durante la marcha.  Con la rodilla flexionada, se puede realizar la rotación de la pierna:\n- Rotación lateral por el músculo vasto lateral.\n- Rotación medial por el músculo vasto medial")

        pixmap = QPixmap("musculos/cuadriceps.jpg")
        self.foto.setPixmap(pixmap)

    def tibial_click(self):
        self.caja_titulo.setText("Tibial")
        self.caja_informacion.clear()
        self.caja_informacion.insertPlainText("El músculo tibial anterior está situado en la parte lateral o externa de la tibia. Parte del cóndilo lateral y de los 2/3 superiores de la superficie superior del cuerpo de la tibia. Ciertas fibras también nacen de la porción adyacente de la membrana interósea, de la superficie profunda de la fascia y del tabique intermuscular que existe entre el mismo tibial anterior y el músculo extensor largo de los dedos. Las fibras musculares originadas en toda la extensión del hueso de la pierna siguen un trayecto descendente, y tienen sus terminaciones a la parte superior de un tendón que aparece en el tercio medio de la pierna. De sus varios puntos de partida, el músculo toma una forma fusiforme con fibras relativamente paralelas al plano de su inserción, terminan en un tendón que comienza en la porción anterior e interna del aspecto dorsal del pie, cerca del tobillo. Luego de recorrer los compartimentos más internos de los ligamentos  crural transverso y crural cruciado, se inserta en la superficie medial o interna del hueso cuneiforme medial y en la base del hueso primer metatarso. En su trayecto, el músculo solapa a los vasos tibiales anteriores y al nervio peroneal, en especial en la porción superior de la pierna. ")

        pixmap = QPixmap("musculos/tibial.jpg")
        self.foto.setPixmap(pixmap)

    def soleo_click(self):
        self.caja_titulo.setText("Soleo")
        self.caja_informacion.clear()
        self.caja_informacion.insertPlainText("El músculo sóleo (musculus soleus) es un músculo ancho y grueso ubicado en la pierna que se encuentra en su cara posterior, debajo y por detrás de los gemelos, estando implicado en la bipedestación. Está estrechamente conectado con el gastrocnemio y algunos anatómicos lo consideran un solo músculo: el tríceps sural. Su nombre deriva de la palabra latina 'solea', que significa 'sandalia'. El sóleo está localizado en el compartimento posterior de la pierna. No todos los mamíferos tienen sóleo, como en el caso del perro. En el caballo, es un vestigio.")

        pixmap = QPixmap("musculos/soleo.jpg")
        self.foto.setPixmap(pixmap)

    def gemelos_click(self):
        self.caja_titulo.setText("Músculo Gastrocnemio")
        self.caja_informacion.clear()
        self.caja_informacion.insertPlainText("El músculo gastrocnemio, también llamado musculus gastrocnemius y popularmente gemelos, por estar separado en dos mitades, está situado en la región posterior de la pierna y es el músculo más superficial de la pantorrilla. Está ubicado sobre el músculo sóleo y se extiende desde los cóndilos femorales, porción superior, hasta el tendón calcáneo en su porción inferior. Es voluminoso, oval, aplanado, con dos cabezas: «medial» y «lateral». Se dice que es un músculo biarticular ya que en su trayecto atraviesa dos articulaciones, la de la rodilla y la del tobillo. ")

        pixmap = QPixmap("musculos/gemelos.jpg")
        self.foto.setPixmap(pixmap)

    def vasto_interno_click(self):
        self.caja_titulo.setText("Vasto interno")
        self.caja_informacion.clear()
        self.caja_informacion.insertPlainText("El músculo vasto medial (Vastus medialis) o vasto interno es la porción más medial, es decir, cercana a la línea media del cuerpo, del músculo cuádriceps. Tiene forma de lágrima, su origen está en la parte inferior de la línea intertrocantérica y termina en la rótula formando el tendón rotuliano o tendón patelar.1​ Actúa de manera coordinada con las otras porciones del cuádriceps en la extension de la pierna, alejándola de la nalga. ")

        pixmap = QPixmap("musculos/vasto_interno.jpg")
        self.foto.setPixmap(pixmap)

    def vasto_externo_click(self):
        self.caja_titulo.setText("Vasto externo")
        self.caja_informacion.clear()
        self.caja_informacion.insertPlainText("El músculo vasto lateral o vasto externo es una porción del músculo cuádriceps. Aplicado a la diáfisis del fémur, se inserta:\n- Por una lámina tendinosa, en el borde anterior e inferior del trocánter mayor.\n- En la rama lateral de trifurcación de la línea áspera.\n- En los dos tercios superiores del labio lateral de la línea áspera.\n- En la parte superior y anterolateral de la diáfisis femoral (ver fémur) y en el tabique intermuscular lateral.")

        pixmap = QPixmap("musculos/vasto_externo.jpg")
        self.foto.setPixmap(pixmap)

    def recto_click(self):
        self.caja_titulo.setText("Musculo recto abdominal")
        self.caja_informacion.clear()
        self.caja_informacion.insertPlainText("El músculo recto del abdomen o músculo recto abdominal (musculus rectus abdominis) forma parte de la pared abdominal y se encuentra por fuera de la línea media del abdomen de los seres humanos y de otros animales. Es un músculo par, largo y aplanado, interrumpido por tres o cuatro intersecciones aponeuróticas, llamadas metámeras y dividido medialmente por una banda de tejido conjuntivo llamada línea alba, superior a la línea arqueada, y está contenido en la vaina de los rectos. Se extiende desde la línea media del pubis hasta el borde inferior de la caja torácica y la apófisis xifoides.1​ Se inserta por medio de un tendón aplanado y corto, el cual tiene dos haces musculares, externo e interno, que están separados por la línea alba. Se extiende desde la sínfisis púbica hasta el apéndice xifoides (extremo inferior del esternón) y los cartílagos adyacentes (quinta, sexta y séptima costillas). Está inervado en la parte superior por los seis últimos nervios intercostales y en la parte inferior por una rama del nervio abdominogenital. El músculo recto se encuentra cruzado por bandas fibrosas, aponeuróticas, en general en número de tres, ubicadas por encima del ombligo, llamadas metámeras. ")

        pixmap = QPixmap("musculos/recto.jpg")
        self.foto.setPixmap(pixmap)

    def supinador_click(self):
        self.caja_titulo.setText("Supinador largo")
        self.caja_informacion.clear()
        self.caja_informacion.insertPlainText("El músculo braquiorradial o supinador largo es un músculo largo del brazo en la región externa y superficial del antebrazo. Actúa flexionando el codo y es capaz también de pronación y supinación, dependiendo de su posición en el antebrazo.")

        pixmap = QPixmap("musculos/supinador.jpg")
        self.foto.setPixmap(pixmap)

    def cuello_click(self):
        self.caja_titulo.setText("Esternocleidomastoideo")
        self.caja_informacion.clear()
        self.caja_informacion.insertPlainText("Músculo esternocleidomastoideo (Sternocleidusmastoideus). Ubicado en la zona anterior y lateral del cuello, interviene en la acción de rotación, flexión e inclinación de la cabeza, es de apariencia larga y robusta, se ubica por debajo en la cara posterior del mango del esternón, y el tercio interno de la clavícula y por encima en la cara interna de la apófisis mastoides, y línea curva occipital superior. También llamado músculo de la mirada poética o músculo esternocleidooccipitomastoideo. Los músculos inspiratorios provocan con su contracción un aumento en el tamaño de la caja torácica que consiguen elevando las costillas que realizan un movimiento de rotación sobre las vértebras, aumentando así el área por lo que la presión en su interior disminuye y por tanto se provoca la entrada de aire. ")

        pixmap = QPixmap("musculos/esternocleidomastoideo.png")
        self.foto.setPixmap(pixmap)

    def frontal_click(self):
        self.caja_titulo.setText("Musculo frontal")
        self.caja_informacion.clear()
        self.caja_informacion.insertPlainText("El músculo frontal (venter frontalis musculi occipitofrontalis) es un músculo cutáneo del cráneo. Algunos autores lo consideran la porción muscular anterior del músculo occipitofrontal. Se halla inervado por los filetes frontales de la rama temporofacial del nervio facial.\nTiene su origen en la galea aponeurótica y se inserta en la piel de manera superior al borde supraorbitario. Este músculo mueve el cuero cabelludo en sentido anterior, eleva las cejas y arruga horizontalmente la piel de la frente.\nSi el músculo frontal se contrae aisladamente, conduce hacia adelante la aponeurosis epicranea, elevando la piel de las cejas. En la expresión de fisonomía el frontal es el músculo de la atención, y la manifiesta en sus diferentes grados. Desde la simple expresión de sorpresa hasta la admiración y el espanto. este es un músculo cuyo objetivo es informar sus movimientos. ")

        pixmap = QPixmap("musculos/frontal.jpg")
        self.foto.setPixmap(pixmap)


app = QApplication(sys.argv)
window = Window()
window.show()
app.exec_()
