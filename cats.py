class Cat:

    def __init__(self, name):
        '''
        Creates a Cat instance.
        '''
        self.name = name
        self.is_happy = True
        self.needs_to_pee = False


    def __call__(self):
        print("MEOW! Meow MEOW MEoW!")


    def give_water(self):
        '''
        Make the Cat instance try to drink water.
        '''
        if self.needs_to_pee:
            raise Exception("YOUR CAT ALREADY NEEDS TO PEE DUDE")

        self.needs_to_pee = True


    def pet(self):
        '''
        Pets the Cat instance.
        '''
        self.is_happy = False
        print(f"{self.name} will tolerate your physical touch, but it doesn't "\
        f"make {self.name} very happy...")


    def use_litterbox(self):
        '''
        The Cat instance urinates via Litterbox method.
        '''
        if not self.needs_to_pee:
            raise Exception("Bro your cat is dehydrated, nothing to pee...")

        self.needs_to_pee = False
        print(f"The Litterbox is a sub-par way for a cat to urinate. Sure, it "\
        f"relieves {self.name}'s urgency to pee, but what about {self.name}'s "\
        f"happiness??")


    def use_bidet(self):
        '''
        The Cat instance urinates via Bidet method.
        '''
        if not self.needs_to_pee:
            raise Exception("Bro your cat is dehydrated, nothing to pee...")

        self.needs_to_pee = False
        self.is_happy = True
        print(f"WOW, the Bidet is a great choice! Not only is {self.name} "\
        f"relieved of pee urgency, but now {self.name} feels like a total QWEEN.")
