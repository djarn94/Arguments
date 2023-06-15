# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

#greeting - part 1
def greet(name, greet=[] ):
    greet = f'Hello, {name}!'
    return greet

print(greet('Nova'))

#force calculator of different planets - part 2
def force(mass = float, body = 'earth'):

    #gravity m/s2
    datasource = {'mercury' : 3.7,
                  'venus' : 8.9,
                  'earth' : 9.8,
                  'moon' : 1.6,
                  'mars' : 3.7,
                  'jupiter' : 23.5,
                  'saturn' : 9.0,
                  'uranus' : 8.7,
                  'neptune' : 11,
                  'pluto' : 0.7
                  }

    force = mass * datasource[body]
    
    return f'{body} has a force of {force}'

#prints the force of mercury
print(force(0.330))

#gravitional pull calculator - part 3
def pull(m1 = float, m2 = float, d = float):
    G = 6673*(10**-11)
    attraction = G * m1 * m2 / (d**2)
    return f'the 2 objects are {attraction} of a Newton attracted towards each other!'


print(pull(800, 1500, 3))
