from jaypore_ci import jci

with jci.Pipeline(image="python:3.11") as p:
    p.job("Hello", "echo 'CI Working! fine '")
