import numpy as np
import matplotlib.pyplot as plt


flcr = [100,120,1000,10000]
llcr = [3.89E-02,3.89E-02,3.89E-02,3.99E-02]

fdatos = open('a15.dat', 'r')
f_datos = []		     #  Creamos una lista para la frecuencia
x_datos = []                #  Creamos una lista para la parte real
y_datos = []                #  Creamos una lista para la parte imaginaria
lineas = fdatos.readlines() # Leemos el fichero línea a línea
for linea in lineas:
     f_single, x_single, y_single = linea.split()     # Se separa cada línea en tres columnas
     f_datos.append(float(f_single)) # Añado el elemento f a la lista f_datos
     x_datos.append(float(x_single)) # Añado el elemento x a la lista x_datos
     y_datos.append(float(y_single)) # Añado el elemento y a la lista y_datos
fdatos.close()


f=np.asarray(f_datos)
X=np.asarray(x_datos)
Y=np.asarray(y_datos)

w = 2 * np.pi*f
vin = 1
C = 215.26*10**(-12)
rl = 9765
#calculo de r y L
L = Y/(w*101.2E-6)
Lc = (-(C*rl**2*w*X**2) + rl*vin*Y - C*rl**2*w*Y**2)/(w*(vin**2 - 2*vin*X + X**2 + C**2*rl**2*w**2*X**2 - 2*C*rl*vin*w*Y + Y**2 + C**2*rl**2*w**2*Y**2))

#np.savetxt('al.dat', L, fmt='%1.4e')
np.savetxt('ind_a15.dat', Lc, fmt='%1.4e')
np.savetxt('mod_a15.dat',(Y**2+X**2)**0.5 , fmt='%1.4e')
np.savetxt('frec_a15.dat',f , fmt='%1.4e')


p = plt.semilogx(f,Y,'b.')
q = plt.semilogx(f,X,'r.')
p = plt.semilogx(f,(Y**2+X**2)**0.5,'g.')


plt.title('X e Y') 
plt.show()
p = plt.semilogx(f,(Y**2+X**2)**0.5,'b.')
plt.title('Módulo') 
plt.show()




p = plt.loglog(f,L,'r.')
plt.loglog(flcr,llcr,'b.')
plt.title('Sin considerar capacitancia parásita') 
plt.xlabel('Frecuencia [Hz]')        # Etiqueta del eje OX
plt.ylabel('Inductancia [H]')        # Etiqueta del eje OY
#plt.savefig('f08.png',dpi=300)
plt.show()


q = plt.loglog(f,Lc,'r.')
plt.loglog(flcr,llcr,'b.')

plt.title('Considerando capacitancia parásita') 
plt.xlabel('Frecuencia [Hz]')        # Etiqueta del eje OX
plt.ylabel('Inductancia [H]')        # Etiqueta del eje OY

#plt.savefig('f08-parasito.png',dpi=300)
plt.show()

