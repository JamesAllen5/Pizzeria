import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","learning_log.settings")

import django
django.setup()

from MainApp.models import Pizza

pizzas = Pizza.objects.all() #same as select * From Topic

for t in pizzas: #print topics
    print(t.id, '   ',t.pizza_name)

t = Pizza.objects.get(id=3) #only print topics that id=1

print(t.pizza_name)
#print(t.date_added)

#print entries
topping = t.topping_set.all()

for e in topping:
    print(e.topping_name)


comment = t.comment_set.all()

for c in comment:
    print(c.comment_entry)
    print(c.date_added)

