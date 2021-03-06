import re

from checks._check import AbstractCheck

regex = {
    '([^\t&|=^><+\-*%\/! ]=[^=]|[^&|=^><+\-*%\/!]=[^= \n])': '=',
    '([^\t ]==|==[^ \n])': '==',
    '([^\t ]!=|!=[^ \n])': '!=',
    '([^\t <]<=|[^<]<=[^ \n])': '<=',
    '([^\t >]>=|[^>]>=[^ \n])': '>=',
    '([^\t ]&&|&&[^ \n])': '&&',
    '([^\t ]\|\||\|\|[^ \n])': '||',
    '([^\t ]\+=|\+=[^ \n])': '+=',
    '([^\t ]-=|-=[^ \n])': '-=',
    '([^\t ]\*=|\*=[^ \n])': '*=',
    '([^\t ]\/=|\/=[^ \n])': '/=',
    '([^\t ]%=|%=[^ \n])': '%=',
    '([^\t ]&=|&=[^ \n])': '&=',
    '([^\t ]\^=|\^=[^ \n])': '^=',
    '([^\t ]\|=|\|=[^ \n])': '|=',
    '([^\t ]\^|\^[^ =\n])': '^',
    '([^\t ]>>[^=]|>>[^ =\n])': '>>',
    '([^\t ]<<[^=]|<<[^ =\n])': '<<',
    '([^\t ]>>=|>>=[^ \n])': '>>=',
    '([^\t ]<<=|<<=[^ \n])': '<<=',
    '([^!]! )': '!',
    '([^a-zA-Z0-9]sizeof )': 'sizeof',
    '([^a-zA-Z)\]]\+\+[^(\[*a-zA-Z])': '++',
    '([^a-zA-Z)\]]--[^\[(*a-zA-Z])': '--'
}


class MisplacedSpace(AbstractCheck):

    def __init__(self, file_name, header_lines):
        self.message = "Missing spaces in operator '{0}'"
        self.file_name = file_name
        self.header_lines = header_lines

    def get_check_id(self):
        return "L3"

    def get_check_level(self):
        return 1

    def check_line(self, line, line_number):
        for misplaced_space in regex:
            if re.search(misplaced_space, line):
                self.fill_error(regex[misplaced_space])
                return 1
        return 0

    def check_function_calls(self, func):
        return 0

    def check_variable_decl(self, var):
        return 0

    def check_function_decl(self, visitor, func):
        return 0

    def check_visitor(self, visitor, lines):
        return 0

    def check_inner(self, file_content, file_contentf):
        return 0