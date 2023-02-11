#Librairies
import streamlit as st

#Fonctions
import functions

st.title("Calculatrice de la capacité d'emprunt")

revenus = st.number_input("Entrez vos revenus mensuels net", value = 2500)
mensualite_max = functions.mensualite_max(revenus)

duree_emprunt = st.number_input("Entrez la durée de l'emprunt (en années)", step = 1, value = 20)
nombre_mensualite = duree_emprunt * 12

taux_credit = st.number_input("Entrez le taux du crédit", step = 0.0001, value = 0.02, format = "%0.4f")
taux_assurance = st.number_input("Entrez le taux d'assurance", step = 0.0001, value = 0.008, format = "%0.4f")

capacite_emprunt = functions.capacite_emprunt(mensualite_max, taux_credit, taux_assurance, nombre_mensualite)
st.write("Votre capacité d'emprunt maximale est de :", capacite_emprunt)

