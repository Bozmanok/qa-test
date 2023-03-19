id_req = '123-abc-321'
name = 'Jack'
surname = 'Lee'
age = 50
type_phone = '1234567890'
method_add = 'add'
method_delete = 'delete'
method_update = 'update'
method_select = 'select'


class DataForAdd:

    data_list_type_field_for_add = [
            (
                '{'
                '"id_req": 123,'
                f'"method": "{method_add}",'
                f'"name": "{name}",'
                f'"surname": "{surname}",'
                f'"phone": "{type_phone}",'
                f'"age": {age}'
                '}'
            ),
            (
                '{'
                f'"id_req": {id_req},'
                f'"method": {method_add},'
                '"name": 345,'
                f'"surname": "{surname}",'
                f'"phone": "{type_phone}",'
                f'"age": {age}'
                '}'
            ),
            (
                '{'
                f'"id_req": {id_req},'
                f'"method": {method_add},'
                f'"name": {name},'
                '"surname": 456,'
                f'"phone": "{type_phone}",'
                f'"age": {age}'
                '}'
            ),
            (
                '{'
                f'"id_req": {id_req},'
                f'"method": {method_add},'
                f'"name": {name},'
                f'"surname": {surname},'
                '"phone": 567,'
                f'"age": {age}'
                '}'
            ),
            (
                '{'
                f'"id_req": {id_req},'
                f'"method": {method_add},'
                f'"name": {name},'
                f'"surname": {surname},'
                f'"phone": {type_phone},'
                f'"age": {str(age)}'
                '}'
            )
        ]

    data_list_without_one_field_for_add = [
            (
                '{'
                f'"method": "{method_add}",'
                f'"name": "{name}",'
                f'"surname": "{surname}",'
                f'"phone": "{type_phone}",'
                f'"age": {age}'
                '}'
            ),
            (
                '{'
                f'"id_req": {id_req},'
                f'"method": {method_add},'
                f'"surname": "{surname}",'
                f'"phone": "{type_phone}",'
                f'"age": {age}'
                '}'
            ),
            (
                '{'
                f'"id_req": {id_req},'
                f'"method": {method_add},'
                f'"name": {name},'
                f'"phone": "{type_phone}",'
                f'"age": {age}'
                '}'
            ),
            (
                '{'
                f'"id_req": {id_req},'
                f'"method": {method_add},'
                f'"name": {name},'
                f'"surname": {surname},'
                f'"age": {age}'
                '}'
            ),
            (
                '{'
                f'"id_req": {id_req},'
                f'"method": {method_add},'
                f'"name": {name},'
                f'"surname": {surname},'
                f'"phone": {type_phone}'
                '}'
            )
        ]

    data_list_field_with_none_for_add = [
            (
                '{'
                '"id_req": None,'
                f'"method": "{method_add}",'
                f'"name": "{name}",'
                f'"surname": "{surname}",'
                f'"phone": "{type_phone}",'
                f'"age": {age}'
                '}'
            ),
            (
                '{'
                f'"id_req": {id_req},'
                f'"method": {method_add},'
                '"name": None,'
                f'"surname": "{surname}",'
                f'"phone": "{type_phone}",'
                f'"age": {age}'
                '}'
            ),
            (
                '{'
                f'"id_req": {id_req},'
                f'"method": {method_add},'
                f'"name": {name},'
                '"surname": None,'
                f'"phone": "{type_phone}",'
                f'"age": {age}'
                '}'
            ),
            (
                '{'
                f'"id_req": {id_req},'
                f'"method": {method_add},'
                f'"name": {name},'
                f'"surname": {surname},'
                '"phone": None,'
                f'"age": {age}'
                '}'
            ),
            (
                '{'
                f'"id_req": {id_req},'
                f'"method": {method_add},'
                f'"name": {name},'
                f'"surname": {surname},'
                f'"phone": {type_phone},'
                '"age": None'
                '}'
            )
        ]


class DataForDelete:

    data_list_type_field_for_delete = [
            (
                '{'
                '"id_req": 123,'
                f'"method": "{method_delete}",'
                f'"phone": "{type_phone}"'
                '}'
            ),
            (
                '{'
                f'"id_req": {id_req},'
                f'"method": {method_delete},'
                '"phone": 567'
                '}'
            )
        ]

    data_list_without_one_field_for_delete = [
            (
                '{'
                f'"method": "{method_delete}",'
                f'"phone": "{type_phone}"'
                '}'
            ),
            (
                '{'
                f'"id_req": {id_req},'
                f'"method": {method_delete}'
                '}'
            )
        ]

    data_list_field_with_none_for_delete = [
            (
                '{'
                '"id_req": None,'
                f'"method": "{method_delete}",'
                f'"phone": "{type_phone}"'
                '}'
            ),
            (
                '{'
                f'"id_req": {id_req},'
                f'"method": {method_delete},'
                '"phone": None'
                '}'
            )
        ]


class DataForUpdate:

    data_list_type_field_for_update = [
            (
                '{'
                '"id_req": 123,'
                f'"method": "{method_update}",'
                f'"name": "{name}",'
                f'"surname": "{surname}",'
                f'"phone": "{type_phone}",'
                f'"age": {age}'
                '}'
            ),
            (
                '{'
                f'"id_req": {id_req},'
                f'"method": {method_update},'
                '"name": 345,'
                f'"surname": "{surname}",'
                f'"phone": "{type_phone}",'
                f'"age": {age}'
                '}'
            ),
            (
                '{'
                f'"id_req": {id_req},'
                f'"method": {method_update},'
                f'"name": {name},'
                '"surname": 456,'
                f'"phone": "{type_phone}",'
                f'"age": {age}'
                '}'
            ),
            (
                '{'
                f'"id_req": {id_req},'
                f'"method": {method_update},'
                f'"name": {name},'
                f'"surname": {surname},'
                '"phone": 567,'
                f'"age": {age}'
                '}'
            ),
            (
                '{'
                f'"id_req": {id_req},'
                f'"method": {method_update},'
                f'"name": {name},'
                f'"surname": {surname},'
                f'"phone": {type_phone},'
                f'"age": {str(age)}'
                '}'
            )
        ]

    data_list_without_one_field_for_update = [
            (
                '{'
                f'"method": "{method_update}",'
                f'"name": "{name}",'
                f'"surname": "{surname}",'
                f'"phone": "{type_phone}",'
                f'"age": {age}'
                '}'
            ),
            (
                '{'
                f'"id_req": {id_req},'
                f'"method": {method_update},'
                f'"surname": "{surname}",'
                f'"phone": "{type_phone}",'
                f'"age": {age}'
                '}'
            ),
            (
                '{'
                f'"id_req": {id_req},'
                f'"method": {method_update},'
                f'"name": {name},'
                f'"phone": "{type_phone}",'
                f'"age": {age}'
                '}'
            ),
            (
                '{'
                f'"id_req": {id_req},'
                f'"method": {method_update},'
                f'"name": {name},'
                f'"surname": {surname},'
                f'"age": {age}'
                '}'
            ),
            (
                '{'
                f'"id_req": {id_req},'
                f'"method": {method_update},'
                f'"name": {name},'
                f'"surname": {surname},'
                f'"phone": {type_phone}'
                '}'
            )
        ]

    data_list_field_with_none_for_update = [
            (
                '{'
                '"id_req": None,'
                f'"method": "{method_update}",'
                f'"name": "{name}",'
                f'"surname": "{surname}",'
                f'"phone": "{type_phone}",'
                f'"age": {age}'
                '}'
            ),
            (
                '{'
                f'"id_req": {id_req},'
                f'"method": {method_update},'
                '"name": None,'
                f'"surname": "{surname}",'
                f'"phone": "{type_phone}",'
                f'"age": {age}'
                '}'
            ),
            (
                '{'
                f'"id_req": {id_req},'
                f'"method": {method_update},'
                f'"name": {name},'
                '"surname": None,'
                f'"phone": "{type_phone}",'
                f'"age": {age}'
                '}'
            ),
            (
                '{'
                f'"id_req": {id_req},'
                f'"method": {method_update},'
                f'"name": {name},'
                f'"surname": {surname},'
                '"phone": None,'
                f'"age": {age}'
                '}'
            ),
            (
                '{'
                f'"id_req": {id_req},'
                f'"method": {method_update},'
                f'"name": {name},'
                f'"surname": {surname},'
                f'"phone": {type_phone},'
                '"age": None'
                '}'
            )
        ]


class DataForSelect:

    data_list_type_field_for_select = [
            (
                '{'
                '"id_req": 123,'
                f'"method": "{method_select}",'
                f'"name": "{name}"'
                '}'
            ),
            (
                '{'
                f'"id_req": {id_req},'
                f'"method": "{method_select}",'
                f'"name": 234'
                '}'
            ),
            (
                '{'
                '"id_req": 123,'
                f'"method": "{method_select}",'
                f'"surname": "{surname}"'
                '}'
            ),
            (
                '{'
                f'"id_req": {id_req},'
                f'"method": "{method_select}",'
                f'"surname": 234'
                '}'
            ),
            (
                '{'
                '"id_req": 123,'
                f'"method": "{method_select}",'
                f'"phone": "{type_phone}"'
                '}'
            ),
            (
                '{'
                f'"id_req": {id_req},'
                f'"method": "{method_select}",'
                f'"phone": 234'
                '}'
            )
        ]

    data_list_without_one_field_for_select = [
            (
                '{'
                f'"id_req": {id_req},'
                f'"method": "{method_select}",'
                '}'
            ),
            (
                '{'
                f'"method": "{method_select}",'
                f'"name": "{name}"'
                '}'
            ),
            (
                '{'
                f'"method": "{method_select}",'
                f'"surname": "{surname}"'
                '}'
            ),
            (
                '{'
                f'"method": "{method_select}",'
                f'"phone": "{type_phone}"'
                '}'
            )
        ]

    data_list_field_with_none_for_select = [
            (
                '{'
                '"id_req": None,'
                f'"method": "{method_select}",'
                f'"name": "{name}"'
                '}'
            ),
            (
                '{'
                f'"id_req": {id_req},'
                f'"method": "{method_select}",'
                f'"name": None'
                '}'
            ),
            (
                '{'
                '"id_req": None,'
                f'"method": "{method_select}",'
                f'"surname": "{surname}"'
                '}'
            ),
            (
                '{'
                f'"id_req": {id_req},'
                f'"method": "{method_select}",'
                f'"surname": None'
                '}'
            ),
            (
                '{'
                '"id_req": None,'
                f'"method": "{method_select}",'
                f'"phone": "{type_phone}"'
                '}'
            ),
            (
                '{'
                f'"id_req": {id_req},'
                f'"method": "{method_select}",'
                f'"phone": None'
                '}'
            )
        ]


class DataForCommon:

    data_list_type_method = [
        (
            '{'
            f'"id_req": {id_req},'
            '"method": 123,'
            f'"name": "{name}",'
            f'"surname": "{surname}",'
            f'"phone": "{type_phone}",'
            f'"age": {age}'
            '}'
        ),
        (
            '{'
            f'"id_req": {id_req},'
            f'"method": 123,'
            f'"name": "{name}"'
            '}'
        ),
        (
            '{'
            f'"id_req": {id_req},'
            '"method": 234,'
            f'"surname": "{surname}"'
            '}'
        ),
        (
            '{'
            f'"id_req": {id_req},'
            '"method": 345,'
            f'"phone": "{type_phone}"'
            '}'
        )
    ]

    data_list_without_field_method = [
        (
            '{'
            f'"id_req": {id_req},'
            f'"name": "{name}",'
            f'"surname": "{surname}",'
            f'"phone": "{type_phone}",'
            f'"age": {age}'
            '}'
        ),
        (
            '{'
            f'"id_req": {id_req},'
            f'"name": "{name}"'
            '}'
        ),
        (
            '{'
            f'"id_req": {id_req},'
            f'"surname": "{surname}"'
            '}'
        ),
        (
            '{'
            f'"id_req": {id_req},'
            f'"phone": "{type_phone}"'
            '}'
        )
    ]

    data_list_method_is_none = [
        (
            '{'
            f'"id_req": {id_req},'
            '"method": None,'
            f'"name": "{name}",'
            f'"surname": "{surname}",'
            f'"phone": "{type_phone}",'
            f'"age": {age}'
            '}'
        ),
        (
            '{'
            f'"id_req": {id_req},'
            f'"method": None,'
            f'"name": "{name}"'
            '}'
        ),
        (
            '{'
            f'"id_req": {id_req},'
            '"method": None,'
            f'"surname": "{surname}"'
            '}'
        ),
        (
            '{'
            f'"id_req": {id_req},'
            '"method": None,'
            f'"phone": "{type_phone}"'
            '}'
        )
    ]
