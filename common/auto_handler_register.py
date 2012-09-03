import os

class AutoHandlerRegister(object):
	def register(self, package_name, path, method_name, handler_dispatcher):
		module_name_list = [m[:-3] for m in os.listdir(path) if m.endswith('.py')]
		for module_name in module_name_list:
			module = __import__(''.join([package_name, '.', module_name]))
			module = getattr(module, module_name)

			for class_name in dir(module):
				class_obj = getattr(module, class_name)
				if hasattr(class_obj, method_name):
					method = getattr(class_obj, method_name)
					method(handler_dispatcher)

		return handler_dispatcher
