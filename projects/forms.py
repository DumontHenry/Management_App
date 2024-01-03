from django.forms import ModelForm
from .models import Task, Project
from django.forms import DateInput


# Defining a new form class named 'TaskForm'
class TaskForm(ModelForm):
    # Nested class Meta inside TaskForm
    class Meta:
        # Specifying the model to which this form is linked
        model = Task  
        # The fields attribute is set to '__all__' to include all fields of the model in the form
        fields = '__all__'  
        # Customizing form widgets for specific fields
        widgets = {
            # Specifying a custom widget for the 'due_date' field
            'due_date': DateInput(
                format='%Y-%m-%d',  # Setting the format of the date
                attrs={'type': 'date'}  # Setting the HTML input type to 'date' for a date picker widget
            ),
        }
"""
In the TaskForm, we also add a widget to display a calendar on the form for the due_date field. 
Django widget handles how the form fields are rendered.


A few points to note about this code:
--> The code starts by defining a form class TaskForm, which is a subclass of ModelForm. ModelForm is a convenient way in Django to create a form directly from a model.
--> Inside the TaskForm, a nested class Meta is defined. This Meta class is used to provide metadata to the TaskForm class.
--> The model attribute inside the Meta class specifies the Django model to which this form corresponds. In your case, it's a model named Task.
--> The fields attribute specifies which fields should be included in the form. By setting it to '__all__', you're including all fields of the Task model.
--> The widgets attribute allows you to customize how the form fields are rendered. In this case, a custom widget DateInput is defined for the due_date field. This widget changes the input format to a date picker in the form.
--> The DateInput widget is being customized further by specifying the date format and setting the HTML input type to 'date'. This ensures that users will have a calendar-like interface to pick dates from in browsers that support the HTML5 date input type.
--> This form can be used in your Django views to handle the creation and editing of Task instances in a way that is directly tied to the fields and behaviors defined in your Task model.
"""