import streamlit as st
from Password_generator_cli import generate_password    
from File_operation import write_password_to_file, read_passwords_from_file

st.title("Password generator app")
st.write("generate a secure password and save it to a file ")

n_letters = st.number_input("How many letters would you like in your password",min_value=0,value=3)
n_numbers = st.number_input("How many numbers would you like in your password",min_value=0,value=3)
n_symbols = st.number_input("How many symbols would you like in your password",min_value=0,value=3)

if st.button("Generate Password"):
   password = generate_password(int(n_letters), int(n_numbers),int(n_symbols))
   st.success(f"Generated Password: {password}")


   write_password_to_file(password)
   st.info("password save to file")

if st.checkbox("show saved passwords"):
   passwords = read_passwords_from_file()


   if passwords:
      st.write("saved passwords:")
      st.markdown("\n".join([f"{password}" for password in passwords]))
   else:
      st.warning("no password saved yet")