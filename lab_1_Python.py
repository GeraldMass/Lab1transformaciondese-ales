from turtle import end_fill
import numpy as np
import matplotlib.pyplot as plt 
import streamlit as st  
import scipy.signal as sg
import pylab as pl 
from re import L, T 

st.title('Laboratorio 1')

k = st.number_input("ingrese el valor de la nueva amplitud")

l = st.number_input("ingrese el valor de la nueva escala")

m = st.number_input("ingrese el valor del desplazamiento")

selectbox = ["-","Señal Senoidal", "Señal Pulso", "Señal Cuadrática", "Señal Exponencial", "Señal Lineal", "Señal Triangular", "Señal Cuadrada","Secuencia de Pulsos"]
selectedbox = st.sidebar.selectbox("Elige el tipo de señal", options = selectbox)


if selectedbox == "Señal Senoidal":
    st.title("Prueba señal senoidal")
    f = st.number_input('Ingrese frecuencia f:')
    amplitude = st.number_input('Ingrese amplitud A:')
    T=6/f
    paso=1/(4*2*np.pi*f)
    t = np.arange(0,T,paso) 
    y = amplitude*np.sin(2*np.pi*f*t)
    fig, ax = plt.subplots()
    pl.xlabel('Tiempo [s]')
    pl.ylabel('Amplitud')
    pl.title('Senoidal')
    ax.plot(t,y)
    st.pyplot(fig) 
    t2=t-m
    ax.plot(t2,y)
    st.pyplot(fig) 
    if k>0:
        y = (k*amplitude)*np.sin(2*np.pi*f*t)
        fig, ax = plt.subplots()
        pl.xlabel('Tiempo [s]')
        pl.ylabel('Amplitud')
        pl.title('Senoidal')
        ax.plot(t,y)
        st.pyplot(fig)
    else:
        y = (amplitude/(-k))*np.sin(2*np.pi*f*t)
        fig, ax = plt.subplots()
        pl.xlabel('Tiempo [s]')
        pl.ylabel('Amplitud')
        pl.title('Senoidal')
        ax.plot(t,y)
        st.pyplot(fig)
    end_fill
 
else:
    if selectedbox == "Señal Exponencial":
        st.title(' Señal Exponencial')
        A = st.number_input('Ingrese el valor de A:')
        b= st.number_input('Ingrese el valor de b:')
        t = np.arange(-0.25,0.25,0.01)
        y = A*np.exp(-b*t)
        fig, ax = plt.subplots()
        pl.xlabel('t [s]')
        pl.ylabel('Amplitud')
        pl.title('Señal Exponencial')
        ax.plot(t,y)
        t2=t-m
        ax.plot(t2,y)
        ax.grid(True)
        st.pyplot(fig)
        if k>0:
            y = (k*A)*np.exp(-b*t)
            fig, ax = plt.subplots()
            pl.xlabel('t [s]')
            pl.ylabel('Amplitud')
            pl.title('Señal Exponencial')
            ax.plot(t,y)
            ax.grid(True)
            st.pyplot(fig) 
        else:
            y = (A/(-k))*np.exp(-b*t)
            fig, ax = plt.subplots()
            pl.xlabel('t [s]')
            pl.ylabel('Amplitud')
            pl.title('Señal Exponencial')
            ax.plot(t,y)
            ax.grid(True)
            st.pyplot(fig)
           
        end_fill
    else:
        if selectedbox ==  "Señal Lineal":
            st.title(' Señal Lineal')
            m = st.number_input('ingrese el valor de la pendiente m:')
            b= st.number_input('ingrese el valor de b:')
            t = np.arange(-5, 5, 0.01)
            y = m*t + b 
            fig, ax = plt.subplots()
            ax.plot(t,y)
            t2=t-m
            ax.plot(t2,y)
            ax.grid(True)
            st.pyplot(fig)
            if k>0:
               y = (m*k)*t + b 
               fig, ax = plt.subplots()
               ax.plot(t,y)
               ax.grid(True)
               st.pyplot(fig)
            else:
               y = (m/(-k))*t + b 
               fig, ax = plt.subplots()
               ax.plot(t,y)
               ax.grid(True)
               st.pyplot(fig)
            end_fill
        else:
            if selectedbox == "Señal Cuadrática":
              st.write("Señal cuadratica y(t)= at^2+bt+c")
              a=st.number_input("introduce el valor de a:")
              b=st.number_input("introduce el valor de b:")
              c=st.number_input("introduce el valor de c:")
              amplitud=st.number_input("introduce el valor de amplitud: ")
              F=st.number_input("introduce el valor de frecuencia:")
              T=1/F
              t=np.arange(0,F,0.01)
              y=(a*t**2+b*t+c)*amplitud
              fig,ax=plt.subplots()
              ax.plot(t,y)
              t2=t-m
              ax.plot(t2,y)
              ax.set_title("Función cuadratica")
              ax.set_xlabel("Eje x")
              ax.set_ylabel("Eje y")
              ax.grid(True)
              st.pyplot(fig)
              if k>0:
                 y=(a*t**2+b*t+c)*(amplitud*k)
                 fig,ax=plt.subplots()
                 ax.plot(t,y)
                 ax.set_title("Función cuadratica")
                 ax.set_xlabel("Eje x")
                 ax.set_ylabel("Eje y")
                 ax.grid(True)
                 st.pyplot(fig)
              else:
                 y=(a*t**2+b*t+c)*(amplitud/(-k))
                 fig,ax=plt.subplots()
                 ax.plot(t,y)
                 ax.set_title("Función cuadratica")
                 ax.set_xlabel("Eje x")
                 ax.set_ylabel("Eje y")
                 ax.grid(True)
                 st.pyplot(fig)
              end_fill
            else:
                if selectedbox == "Señal Pulso":
                   st.write("Señal pulso")
                   amplitud=st.number_input("introduce el valor de amplitud:   ")
                   ancho=st.number_input("introduce el valor de ancho:")
                   t= np.arange(-ancho,ancho,0.01)
                   y=np.zeros(len(t))
                   Y= t*0
                   y[(t>-ancho/2) & (t< ancho/2)]=amplitud
                   fig,ax=plt.subplots()
                   t2=t-m
                   ax.plot(t2,y)
                   ax.plot(t,y)
                   ax.set_title("Función Pulso")
                   ax.set_xlabel("t[s]")
                   ax.set_ylabel("Amplitud")
                   ax.grid(True)
                   st.pyplot(fig)
                   if k>0:
                     y[(t>-ancho/2) & (t< ancho/2)]=amplitud
                     fig,ax=plt.subplots()
                     ax.plot(t,(y*k))
                     ax.set_title("Función Pulso")
                     ax.set_xlabel("t[s]")
                     ax.set_ylabel("Amplitud")
                     ax.grid(True)
                     st.pyplot(fig)
                   else:
                     y[(t>-ancho/2) & (t< ancho/2)]=amplitud
                     fig,ax=plt.subplots()
                     ax.plot(t,(y/(-k)))
                     ax.set_title("Función Pulso")
                     ax.set_xlabel("t[s]")
                     ax.set_ylabel("Amplitud")
                     ax.grid(True)
                     st.pyplot(fig)
                   end_fill
                else: 
                    if selectedbox == "Señal Triangular":
                        st.write("Señal triangular")
                        amplitud=st.number_input("introduce el valor de amplitud:")
                        F=st.number_input("introduce el valor de frecuencia: ")
                        t=np.arange(0,F,0.01)
                        y = sg.sawtooth(2*np.pi*F*t)*amplitud
                        fig,ax=plt.subplots()
                        t2=t-m
                        ax.plot(t2,y)
                        ax.plot(t,y)
                        ax.set_title("Función triangular")
                        ax.set_xlabel("Eje x")
                        ax.set_ylabel("Eje y")
                        ax.grid(True)
                        st.pyplot(fig)
                        if k>0:
                            y = sg.sawtooth(2*np.pi*F*t)*(amplitud*k)
                            fig,ax=plt.subplots()
                            ax.plot(t,y)
                            ax.set_title("Función triangular")
                            ax.set_xlabel("Eje x")
                            ax.set_ylabel("Eje y")
                            ax.grid(True)
                            st.pyplot(fig)
                        else:
                            y = sg.sawtooth(2*np.pi*F*t)*(amplitud/(-k))
                            fig,ax=plt.subplots()
                            ax.plot(t,y)
                            ax.set_title("Función triangular")
                            ax.set_xlabel("Eje x")
                            ax.set_ylabel("Eje y")
                            ax.grid(True)
                            st.pyplot(fig)
                        end_fill
                    else:
                        if selectedbox == "Señal Cuadrada":
                            st.write("Señal cuadrada")
                            amplitud=st.number_input("introduce el valor de amplitud:  ")
                            F=st.number_input("introduce el valor de frecuencia:  ")
                            t=np.arange(0,F,0.01)
                            y=sg.square(2*np.pi*F*t)*amplitud
                            fig,ax=plt.subplots()
                            t2=t-m
                            ax.plot(t2,y)
                            ax.plot(t,y)
                            ax.set_title("Función Cuadrada")
                            ax.set_xlabel("Eje x")
                            ax.set_ylabel("Eje y")
                            ax.grid(True)
                            st.pyplot(fig)
                            if k>0:
                               y=sg.square(2*np.pi*F*t)*(amplitud*k)
                               fig,ax=plt.subplots()
                               ax.plot(t,y)
                               ax.set_title("Función Cuadrada")
                               ax.set_xlabel("Eje x")
                               ax.set_ylabel("Eje y")
                               ax.grid(True)
                               st.pyplot(fig)
                            else:
                               y=sg.square(2*np.pi*F*t)*(amplitud/(-k))
                               fig,ax=plt.subplots()
                               ax.plot(t,y)
                               ax.set_title("Función Cuadrada")
                               ax.set_xlabel("Eje x")
                               ax.set_ylabel("Eje y")
                               ax.grid(True)
                               st.pyplot(fig)
                            end_fill
                        else: 
                            if selectedbox == "Secuencia de Pulsos":
                               st.sidebar.write("Señal de secuencia de pulsos")
                               y = st.text_input("introduzca los valores de los pulsos y separelos con coma ','" , "0,0,0,0,0 ")
                               y = y.split(',')
                               y =[int(i) for i in y]
                               t = st.text_input("introduzca la posicion de cada pulso y separelo por coma ','", "1,2,3,4,5")
                               t = t.split(',')
                               t =[int(i) for i in t]
                               fig,ax=plt.subplots()
                               t2=t-m
                               ax.stem(t2,y)
                               ax.stem(t,y)
                               ax.set_title("secuencia de pulsos")
                               ax.set_xlabel("Eje t")
                               ax.set_ylabel("Eje y")
                               ax.grid(True)
                               st.pyplot(fig)
                               end_fill
                            end_fill
                        end_fill
                    end_fill
                end_fill
            end_fill
        end_fill
    end_fill
end_fill



                               


                            



    

