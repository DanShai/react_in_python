
# dummy defs to shut up the python linter!
# React.createElement(
#   type,
#   [props],
#   [...children]
# )

# __pragma__ ('skip')

class lib:
    def __call__(self,*args,**kwargs):
        pass

    @classmethod
    def createElement(cls,*args,**kwargs):
        pass
    @classmethod
    def render(cls,e,p):
        pass
    @classmethod
    def useState(cls,e):
        pass
    @classmethod
    def useEffect(cls,e,a):
        pass


class document:
    @classmethod
    def getElementById(cls, x):
        pass
    @classmethod
    def addEventListener(cls, x,y):
        pass 

def require(l):
    return lib()

# __pragma__ ('noskip')


React = require('react')
ReactDOM = require('react-dom')
axios = require('axios')
polyfill = require("@babel/polyfill")  # required by async/await
createElement = React.createElement
useState = React.useState
useEffect = React.useEffect

# react render 
def render(current, props, root):
    def main():
        ReactDOM.render(
            React.createElement(current, props),
            document.getElementById(root)
        )

    document.addEventListener("DOMContentLoaded", main)
