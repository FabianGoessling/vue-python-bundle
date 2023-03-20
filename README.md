# UPDATE 20.03.2023
The example of this repo is carried out in detail by the `vbuild`package - so use this package. See the example folder for a `vbuild` variant.

# Vue-python-bundle

A base setup for using [vue](https://vuejs.org) components **without** a dedicated frontend server.

While for a fully fledged application a seperated frontend is the better choice, the method here is a nice start for prototyping. There are [several methods](https://vuejsdevelopers.com/2017/03/24/vue-js-component-templates/) for using the vue.js components. Coming from a more backend centric python background (fastapi, flask, django) defining a modular vue component directly inside the html template never felt like a *good way*. On the other hand the .vue single file components (SFC) require to setup a dedicated frontend server, which felt like a overkill for prototyping. 

Thus this repository shows an example for using SFC without the frontend server. The idea is to define standard vue components and serve these by a fast api powered REST endpoint. The html template loads a jsonified version of all components by an axios call and attaches all components to the Vue instance.


# Installation

Simply install the project by 
```
poetry install
```
followed by the usual uvicorn call:
```
uvicorn main:app --reload
```

# Component attributes
The python 'VueComponent' currently only parses the template, data and prop tags, but extending this is straightforward, if you take a look at the used regex. Note that the examples additionally use vuetify, but this is not required at all.

# Styles
Styling inside the components currently requires to define the styles inside the data property of the vue component instead of the style tag. If you manage to make the `<style>` tag work, let me know!

