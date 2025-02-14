import cv2
from cvzone.HandTrackingModule import HandDetector

video = cv2.VideoCapture(0)
video.set(3,1280)
video.set(4,720)

detector = HandDetector()
desenho = []

while True:
    check,img = video.read() #Ler a imagem
    resultado = detector.findHands(img, draw= True) #Identificar a mão e colocar dentro de um retângulo
    hand = resultado[0] # primeira mão que aparece.

    if hand:
        lmlist = hand[0]['lmList'] #Permite saber as coordenadas de cada ponto presente no dedo.
        dedos = detector.fingersUp(hand[0]) #detectar os dedos.
        dedosLev = dedos.count(1) #contar quantos dedos estão levandos.
        #print(dedosLev) imprime na saída do código a quantidade de dedos levantados.

        if dedosLev==1: #Se apenas um dedo estiver levantado.
            x,y = lmlist[8][0], lmlist[8][1]
            cv2.circle(img, (x,y), 15, (0,0,255), cv2.FILLED) #desenha um círculo vermelho na ponta do dedo indicador.
            desenho.append((x,y))  #Faz um desenho com os dedos utilizando o conceito de matriz.
        elif dedosLev != 1 and dedosLev != 3: #Se dois dedos estiverem levantados
            desenho.append((0,0))
        elif dedosLev ==3:
            desenho = []

        for id, ponto in enumerate(desenho):
            x, y = ponto[0], ponto[1]
            cv2.circle(img, (x,y), 10, (0,0,255), cv2.FILLED)
            
            if id >=1:
                ax, ay = desenho[id-1][0], desenho[id-1][1]
                if x!=0 and ax!=0:
                    cv2.line(img, (x,y), (ax,ay), (0,0,255), 20)
    
    cv2.imshow("img", img)
    if cv2.waitKey(1)==27:
        break