# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

#greeting - part 1
def greet(name, greeting = 'Hello, <name>!'):
  greeting_template = greeting.replace("<name>",name)
  return greeting_template

print(greet("Doc"))
print(greet('Bob', "What's up, <name>!"))

#force calculator of different planets - part 2
def force(mass = float, body = 'earth'):

    #gravity m/s2
    datasource = {'mercury' : 3.7,
                  'venus' : 8.9,
                  'earth' : 9.8,
                  'moon' : 1.6,
                  'mars' : 3.7,
                  'jupiter' : 23.1,
                  'saturn' : 9.0,
                  'uranus' : 8.7,
                  'neptune' : 11,
                  'pluto' : 0.7
                  }

    force = mass * datasource[body]
    
    return force

#prints the force of mercury
print(force(9.9))

#gravitional pull calculator - part 3
def pull(m1, m2, d):
    G = 6.674*(10**-11)
    pull = G * m1 * m2 / (d**2)
    return pull


print(round(pull(800, 1500, 3),10))
print(round(pull(0.1,5972 * (10**24),6.371*(10**6)),30))