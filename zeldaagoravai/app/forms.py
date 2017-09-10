from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_wtf import Form
from flask_mysqldb import MySQL
from wtforms import StringField, TextAreaField, PasswordField, BooleanField
from passlib.hash import sha256_crypt
from functools import wraps
from wtforms.validators import DataRequired

#Cadastra Login
class LoginForm(Form):
    login = StringField('Nome de Usuário', validators=[DataRequired('Nome de Usuário é obrigatório')])
    senha = PasswordField('Senha', validators=[DataRequired('Senha é obrigatório')])

#Cadastra Funcionario
class CadastraFuncionarioForm(Form):
    funcionario_nome = StringField('Nome Funcionário', validators=[DataRequired('Nome de Funcionário é obrigatório')])
    funcionario_login = StringField('Login Funcionário', validators=[DataRequired('Login do Funcionário é obrigatório')])
    funcionario_senha = PasswordField('Senha', validators=[DataRequired('Senha é obrigatório')])
    funcionario_setor_id = StringField ('Setor', validators=[DataRequired()])
    

#Cadastra Setor
class CadastraSetorForms(Form):
        setor_nome = StringField('Nome Setor', validators=[DataRequired('Nome do Setor é obrigatório')])

