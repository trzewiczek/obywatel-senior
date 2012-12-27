#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Main access point to the kuklok prototype
'''

from bottle import request, redirect, route, run, template, static_file


# -- routes
@route('/')
def index():
    '''
    Main page view
    '''
    redirect('/blog')

@route('/blog')
def blog():
    '''
    Main page view
    '''
    return template('blog')

@route('/blog/new')
def blog_new():
    '''
    Main page view
    '''
    return template('blog')

@route('/notatki')
def notatki():
    '''
    Main page view
    '''
    return template('blog')


@route('/static/<path:path>')
def serve_files(path):
    '''
    Static files route
    '''
    return static_file(path, root='./static/')


# -- run the app
if __name__ == '__main__':
    run(host='localhost', port=8080, reloader=True)
