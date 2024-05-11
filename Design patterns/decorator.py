"""
	Decorator
	- a structural pattern that allows adding new behaviors to objects dynamically
	by placing them inside special wrapper objects, called decorators.
"""
import abc

class Page(abc.ABC):
    """
    Abstract base class representing a webpage.
    All pages must implement a show method.
    """
    @abc.abstractmethod
    def show(self):
        pass


class AuthenticatedPage(Page):
    """
    A concrete page that requires authentication.
    """
    def show(self):
        print('Welcome to the authenticated page')


class AnonymousPage(Page):
    """
    A concrete page that does not require authentication.
    """
    def show(self):
        print('Welcome to the anonymous page')


class PageDecorator(Page, abc.ABC):
    """
    Abstract decorator class for pages, implementing the Page interface.
    """
    def __init__(self, component):
        self._component = component

    @abc.abstractmethod
    def show(self):
        pass


class AuthenticationDecorator(PageDecorator):
    """
    Decorator that adds authentication to pages.
    """
    def show(self):
        if self.authenticate():
            self._component.show()
        else:
            print('Authentication failed.')

    def authenticate(self):
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        return username == 'admin' and password == 'secret'


def client_code():
    """
    Client code to demonstrate the use of decorators.
    """
    page = AuthenticatedPage()
    decorated_page = AuthenticationDecorator(page)
    decorated_page.show()

client_code()
