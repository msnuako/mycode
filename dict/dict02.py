'''Alta3 Research | RZFeeser
   Using the .get() method with Python dict types - The concepts explored in this example may be used within Ansible playbooks to access variable data.'''

def main():
    '''a short exploration of dictionaries'''

    # create a dictionary
    switch = {'hostname': 'sw-1', 'ip': '10.0.1.1', 'version': '1.2', 'vendor': 'cisco'}

    # display parts of the dictionary
    print( switch['hostname'] )
    print( switch['ip'] )

    # request a 'fake' key with .get() method
    print( "First test - .get()" )
    print( switch.get('lynx') )

    print( "Second test - .get()" )
    print( switch.get('lynx', "THE KEY IS IN ANOTHER CASTLE!") )

    print( "Third test - .get()" )
    print( switch.get('version') )
    
# best practice technique to call our python script
if __name__ == "__main__":
    main()     # calls the "main" function to run
