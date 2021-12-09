FileCode(
    body=[
        ContractDefn(
            annotations=None,
            name=Ident(symbol=Token("__ANON_17", "CW20")),
            body=[
                ErrorDefn(
                    annotations=None,
                    defn=EnumVariantStruct(
                        name=Ident(symbol=Token("__ANON_17", "ImproperFormat")),
                        members=[
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_16", "user")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_16", "Addr"))
                                ),
                            ),
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_16", "input")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_16", "String"))
                                ),
                            ),
                        ],
                    ),
                ),
                [
                    ErrorDefn(
                        annotations=[
                            Annotation(
                                items=[
                                    SimplePath(
                                        parts=[
                                            Ident(
                                                symbol=Token("__ANON_16", "annotations")
                                            )
                                        ]
                                    )
                                ]
                            )
                        ],
                        defn=EnumVariantStruct(
                            name=Ident(symbol=Token("__ANON_17", "NotEnabled")),
                            members=[
                                TypeAssign(
                                    annotations=None,
                                    name=Ident(symbol=Token("__ANON_16", "req_level")),
                                    type=EnumDefn(
                                        annotations=None,
                                        name=Ident(symbol=Token("__ANON_17", "Levels")),
                                        variants=[
                                            EnumVariantDefn(
                                                annotations=Annotation(
                                                    items=[
                                                        SimplePath(
                                                            parts=[
                                                                Ident(
                                                                    symbol=Token(
                                                                        "__ANON_16",
                                                                        "item",
                                                                    )
                                                                )
                                                            ]
                                                        )
                                                    ]
                                                ),
                                                variant=EnumVariantUnit(
                                                    name=Ident(
                                                        symbol=Token(
                                                            "__ANON_17", "Admin"
                                                        )
                                                    )
                                                ),
                                            ),
                                            EnumVariantDefn(
                                                annotations=None,
                                                variant=EnumVariantUnit(
                                                    name=Ident(
                                                        symbol=Token(
                                                            "__ANON_17", "Student"
                                                        )
                                                    )
                                                ),
                                            ),
                                        ],
                                    ),
                                )
                            ],
                        ),
                    ),
                    ErrorDefn(
                        annotations=None,
                        defn=EnumVariantUnit(
                            name=Ident(symbol=Token("__ANON_17", "Unauthorized"))
                        ),
                    ),
                    ErrorDefn(
                        annotations=None,
                        defn=EnumVariantStruct(
                            name=Ident(symbol=Token("__ANON_17", "InsufficientFunds")),
                            members=[
                                TypeAssign(
                                    annotations=None,
                                    name=Ident(symbol=Token("__ANON_16", "balance")),
                                    type=Typename(
                                        name=Ident(symbol=Token("__ANON_16", "Uint128"))
                                    ),
                                ),
                                TypeAssign(
                                    annotations=None,
                                    name=Ident(symbol=Token("__ANON_16", "needed")),
                                    type=Typename(
                                        name=Ident(symbol=Token("__ANON_16", "Uint128"))
                                    ),
                                ),
                            ],
                        ),
                    ),
                ],
                EventDefn(
                    annotations=None,
                    defn=EnumVariantStruct(
                        name=Ident(symbol=Token("__ANON_17", "Action")),
                        members=[
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_16", "method")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_16", "String"))
                                ),
                            ),
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_16", "owner")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_16", "String"))
                                ),
                            ),
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_16", "count")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_16", "String"))
                                ),
                            ),
                        ],
                    ),
                ),
                [
                    EventDefn(
                        annotations=None,
                        defn=EnumVariantStruct(
                            name=Ident(symbol=Token("__ANON_17", "Increment")),
                            members=[],
                        ),
                    ),
                    EventDefn(
                        annotations=None,
                        defn=EnumVariantStruct(
                            name=Ident(symbol=Token("__ANON_17", "Reset")),
                            members=[
                                TypeAssign(
                                    annotations=None,
                                    name=Ident(symbol=Token("__ANON_16", "method")),
                                    type=Typename(
                                        name=Ident(symbol=Token("__ANON_16", "String"))
                                    ),
                                )
                            ],
                        ),
                    ),
                ],
                ItemDefn(
                    annotations=None,
                    key=Ident(symbol=Token("__ANON_16", "curr_num")),
                    type=Typename(name=Ident(symbol=Token("__ANON_16", "i32"))),
                ),
                MapDefn(
                    annotations=None,
                    prefix=Ident(symbol=Token("__ANON_16", "balances")),
                    keys=[
                        MapKey(
                            key=None,
                            type=Typename(
                                name=Ident(symbol=Token("__ANON_16", "Addr"))
                            ),
                        )
                    ],
                    value=Typename(name=Ident(symbol=Token("__ANON_16", "Uint128"))),
                ),
                [
                    ItemDefn(
                        annotations=None,
                        key=Ident(symbol=Token("__ANON_16", "config")),
                        type=StructCDefn(
                            annotations=None,
                            name=Ident(symbol=Token("__ANON_17", "ConfigData")),
                            members=[
                                TypeAssign(
                                    annotations=None,
                                    name=Ident(symbol=Token("__ANON_16", "owner")),
                                    type=Typename(
                                        name=Ident(symbol=Token("__ANON_16", "Addr"))
                                    ),
                                ),
                                TypeAssign(
                                    annotations=None,
                                    name=Ident(symbol=Token("__ANON_16", "count")),
                                    type=Typename(
                                        name=Ident(symbol=Token("__ANON_16", "i32"))
                                    ),
                                ),
                                TypeAssign(
                                    annotations=None,
                                    name=Ident(
                                        symbol=Token("__ANON_16", "fee_percent")
                                    ),
                                    type=Typename(
                                        name=Ident(symbol=Token("__ANON_16", "Decimal"))
                                    ),
                                ),
                            ],
                        ),
                    ),
                    MapDefn(
                        annotations=None,
                        prefix=Ident(symbol=Token("__ANON_16", "token_balances")),
                        keys=[
                            MapKey(
                                key=Ident(symbol=Token("__ANON_16", "user")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_16", "Addr"))
                                ),
                            ),
                            MapKey(
                                key=None,
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_16", "Addr"))
                                ),
                            ),
                            MapKey(
                                key=Ident(symbol=Token("__ANON_16", "bucket")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_16", "u32"))
                                ),
                            ),
                        ],
                        value=Typename(
                            name=Ident(symbol=Token("__ANON_16", "Uint128"))
                        ),
                    ),
                ],
                InstantiateDefn(
                    annotations=None,
                    args=[
                        TypeAssign(
                            annotations=None,
                            name=Ident(symbol=Token("__ANON_16", "count")),
                            type=Typename(name=Ident(symbol=Token("__ANON_16", "i32"))),
                        ),
                        TypeAssign(
                            annotations=None,
                            name=Ident(symbol=Token("__ANON_16", "fee_percent")),
                            type=Typename(name=Ident(symbol=Token("__ANON_16", "Dec"))),
                        ),
                    ],
                    body=[
                        AssignStmt(
                            lhs=MemberAccessExpr(
                                item=Ident(symbol=Token("__ANON_21", "$state")),
                                member=Ident(symbol=Token("__ANON_16", "config")),
                            ),
                            assign_op=Token("EQUAL", "="),
                            rhs=StructVal(
                                name=Ident(symbol=Token("__ANON_17", "ConfigData")),
                                members=[
                                    StructValAssign(
                                        name=Ident(symbol=Token("__ANON_16", "owner")),
                                        value=MemberAccessExpr(
                                            item=Ident(
                                                symbol=Token("__ANON_20", "$env")
                                            ),
                                            member=Ident(
                                                symbol=Token("__ANON_16", "sender")
                                            ),
                                        ),
                                    ),
                                    StructValAssign(
                                        name=Ident(symbol=Token("__ANON_16", "count")),
                                        value=Ident(symbol=Token("__ANON_16", "count")),
                                    ),
                                    StructValAssign(
                                        name=Ident(
                                            symbol=Token("__ANON_16", "fee_percent")
                                        ),
                                        value=Ident(
                                            symbol=Token("__ANON_16", "fee_percent")
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        EmitStmt(
                            expr=FnCallExpr(
                                fn_name=SimplePath(
                                    parts=[Ident(symbol=Token("__ANON_16", "Action"))]
                                ),
                                args=[
                                    String(
                                        value=Token("ESCAPED_STRING", '"instantiate"')
                                    ),
                                    MemberAccessExpr(
                                        item=Ident(symbol=Token("__ANON_20", "$env")),
                                        member=Ident(
                                            symbol=Token("__ANON_16", "sender")
                                        ),
                                    ),
                                    Ident(symbol=Token("__ANON_16", "count")),
                                ],
                            )
                        ),
                    ],
                ),
                ExecDefn(
                    annotations=None,
                    name=Ident(symbol=Token("__ANON_16", "msg_name_snake_case")),
                    args=[
                        TypeAssign(
                            annotations=None,
                            name=Ident(symbol=Token("__ANON_16", "arg1")),
                            type=Typename(name=Ident(symbol=Token("__ANON_16", "u32"))),
                        ),
                        TypeAssign(
                            annotations=None,
                            name=Ident(symbol=Token("__ANON_16", "arg2")),
                            type=ParamzdTypeExpr(
                                base_type=Typename(
                                    name=Ident(symbol=Token("__ANON_16", "Option"))
                                ),
                                param=Typename(
                                    name=Ident(symbol=Token("__ANON_16", "String"))
                                ),
                            ),
                        ),
                    ],
                    body=[],
                ),
                [
                    ExecDefn(
                        annotations=None,
                        name=Ident(symbol=Token("__ANON_16", "increment")),
                        args=[],
                        body=[
                            AssignStmt(
                                lhs=MemberAccessExpr(
                                    item=MemberAccessExpr(
                                        item=Ident(symbol=Token("__ANON_21", "$state")),
                                        member=Ident(
                                            symbol=Token("__ANON_16", "config")
                                        ),
                                    ),
                                    member=Ident(symbol=Token("__ANON_16", "count")),
                                ),
                                assign_op=Token("__ANON_5", "+="),
                                rhs=Integer(value=Token("__ANON_23", "1")),
                            ),
                            IfExpr(
                                if_clause=IfClause(
                                    predicate=InfixOpExpr(
                                        lhs=MemberAccessExpr(
                                            item=MemberAccessExpr(
                                                item=Ident(
                                                    symbol=Token("__ANON_21", "$state")
                                                ),
                                                member=Ident(
                                                    symbol=Token("__ANON_16", "config")
                                                ),
                                            ),
                                            member=Ident(
                                                symbol=Token("__ANON_16", "count")
                                            ),
                                        ),
                                        op=Token("LESSTHAN", "<"),
                                        rhs=Integer(value=Token("__ANON_23", "2")),
                                    ),
                                    body=[
                                        StructVal(
                                            name=Ident(
                                                symbol=Token("__ANON_17", "Intensity")
                                            ),
                                            members=[
                                                StructValAssign(
                                                    name=Ident(
                                                        symbol=Token(
                                                            "__ANON_16", "item"
                                                        )
                                                    ),
                                                    value=Integer(
                                                        value=Token("__ANON_23", "23")
                                                    ),
                                                ),
                                                StructValAssign(
                                                    name=Ident(
                                                        symbol=Token(
                                                            "__ANON_16", "power23"
                                                        )
                                                    ),
                                                    value=Integer(
                                                        value=Token(
                                                            "__ANON_23", "722391"
                                                        )
                                                    ),
                                                ),
                                                StructValAssign(
                                                    name=Ident(
                                                        symbol=Token(
                                                            "__ANON_16", "my_power"
                                                        )
                                                    ),
                                                    value=FnCallExpr(
                                                        fn_name=SimplePath(
                                                            parts=[
                                                                Ident(
                                                                    symbol=Token(
                                                                        "__ANON_16",
                                                                        "ally",
                                                                    )
                                                                )
                                                            ]
                                                        ),
                                                        args=[
                                                            String(
                                                                value=Token(
                                                                    "ESCAPED_STRING",
                                                                    '"call"',
                                                                )
                                                            ),
                                                            Integer(
                                                                value=Token(
                                                                    "__ANON_23", "12"
                                                                )
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                        )
                                    ],
                                ),
                                else_if_clauses=None,
                                else_body=None,
                            ),
                        ],
                    ),
                    ExecDefn(
                        annotations=None,
                        name=Ident(symbol=Token("__ANON_16", "reset")),
                        args=[
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_16", "count")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_16", "i32"))
                                ),
                            )
                        ],
                        body=[
                            IfExpr(
                                if_clause=IfClause(
                                    predicate=MemberAccessExpr(
                                        item=MemberAccessExpr(
                                            item=InfixOpExpr(
                                                lhs=MemberAccessExpr(
                                                    item=Ident(
                                                        symbol=Token(
                                                            "__ANON_20", "$env"
                                                        )
                                                    ),
                                                    member=Ident(
                                                        symbol=Token(
                                                            "__ANON_16", "sender"
                                                        )
                                                    ),
                                                ),
                                                op=Token("__ANON_13", "!="),
                                                rhs=Ident(
                                                    symbol=Token("__ANON_21", "$state")
                                                ),
                                            ),
                                            member=Ident(
                                                symbol=Token("__ANON_16", "config")
                                            ),
                                        ),
                                        member=Ident(
                                            symbol=Token("__ANON_16", "owner")
                                        ),
                                    ),
                                    body=[
                                        FailStmt(
                                            expr=Ident(
                                                symbol=Token(
                                                    "__ANON_16", "Unauthorized"
                                                )
                                            )
                                        )
                                    ],
                                ),
                                else_if_clauses=None,
                                else_body=None,
                            ),
                            AssignStmt(
                                lhs=MemberAccessExpr(
                                    item=MemberAccessExpr(
                                        item=Ident(symbol=Token("__ANON_21", "$state")),
                                        member=Ident(
                                            symbol=Token("__ANON_16", "config")
                                        ),
                                    ),
                                    member=Ident(symbol=Token("__ANON_16", "count")),
                                ),
                                assign_op=Token("EQUAL", "="),
                                rhs=Ident(symbol=Token("__ANON_16", "count")),
                            ),
                        ],
                    ),
                ],
                QueryDefnFn(
                    annotations=None,
                    name=Ident(symbol=Token("__ANON_16", "count")),
                    args=[],
                    response_type=StructCDefn(
                        annotations=None,
                        name=Ident(symbol=Token("__ANON_17", "CountResponse")),
                        members=[
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_16", "count")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_16", "i32"))
                                ),
                            )
                        ],
                    ),
                    body=[
                        StructVal(
                            name=Ident(symbol=Token("__ANON_17", "CountResponse")),
                            members=[
                                StructValAssign(
                                    name=Ident(symbol=Token("__ANON_16", "count")),
                                    value=MemberAccessExpr(
                                        item=MemberAccessExpr(
                                            item=Ident(
                                                symbol=Token("__ANON_21", "$state")
                                            ),
                                            member=Ident(
                                                symbol=Token("__ANON_16", "config")
                                            ),
                                        ),
                                        member=Ident(
                                            symbol=Token("__ANON_16", "count")
                                        ),
                                    ),
                                )
                            ],
                        )
                    ],
                ),
                QueryDefnFn(
                    annotations=None,
                    name=Ident(symbol=Token("__ANON_16", "item")),
                    args=[],
                    response_type=StructCDefn(
                        annotations=None,
                        name=Ident(symbol=Token("__ANON_17", "ItemResponse")),
                        members=[
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_16", "item")),
                                type=TupleType(
                                    members=[
                                        Option(
                                            wrapped=VectorType(
                                                item=Typename(
                                                    name=Ident(
                                                        symbol=Token("__ANON_16", "int")
                                                    )
                                                )
                                            )
                                        ),
                                        RefType(
                                            wrapped=RefType(
                                                wrapped=VectorType(
                                                    item=TypePath(
                                                        parts=[
                                                            Typename(
                                                                name=Ident(
                                                                    symbol=Token(
                                                                        "__ANON_16",
                                                                        "Fire",
                                                                    )
                                                                )
                                                            ),
                                                            Typename(
                                                                name=Ident(
                                                                    symbol=Token(
                                                                        "__ANON_16",
                                                                        "boy",
                                                                    )
                                                                )
                                                            ),
                                                        ]
                                                    )
                                                )
                                            )
                                        ),
                                        StructUnitDefn(
                                            annotations=None,
                                            name=Ident(
                                                symbol=Token("__ANON_17", "Unit")
                                            ),
                                        ),
                                        StructCDefn(
                                            annotations=None,
                                            name=Ident(
                                                symbol=Token("__ANON_17", "Tiger")
                                            ),
                                            members=[
                                                TypeAssign(
                                                    annotations=None,
                                                    name=Ident(
                                                        symbol=Token(
                                                            "__ANON_16", "item"
                                                        )
                                                    ),
                                                    type=Option(
                                                        wrapped=Typename(
                                                            name=Ident(
                                                                symbol=Token(
                                                                    "__ANON_16", "u32"
                                                                )
                                                            )
                                                        )
                                                    ),
                                                )
                                            ],
                                        ),
                                    ]
                                ),
                            )
                        ],
                    ),
                    body=None,
                ),
                QueryDefnResponds(
                    annotations=None,
                    name=Ident(symbol=Token("__ANON_16", "user_balance_for_token")),
                    args=[
                        TypeAssign(
                            annotations=None,
                            name=Ident(symbol=Token("__ANON_16", "user")),
                            type=Typename(
                                name=Ident(symbol=Token("__ANON_16", "Addr"))
                            ),
                        ),
                        TypeAssign(
                            annotations=None,
                            name=Ident(symbol=Token("__ANON_16", "token")),
                            type=Typename(
                                name=Ident(symbol=Token("__ANON_16", "Addr"))
                            ),
                        ),
                    ],
                    response_defn=[
                        TypeAssignAndSet(
                            type_assign=TypeAssign(
                                annotations=[
                                    Annotation(
                                        items=[
                                            FnCallExpr(
                                                fn_name=SimplePath(
                                                    parts=[
                                                        Ident(
                                                            symbol=Token(
                                                                "__ANON_16", "echo"
                                                            )
                                                        )
                                                    ]
                                                ),
                                                args=[
                                                    String(
                                                        value=Token(
                                                            "ESCAPED_STRING", '"hello"'
                                                        )
                                                    )
                                                ],
                                            )
                                        ]
                                    )
                                ],
                                name=Ident(symbol=Token("__ANON_16", "user")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_16", "Addr"))
                                ),
                            ),
                            value=Ident(symbol=Token("__ANON_16", "user")),
                        ),
                        TypeAssignAndSet(
                            type_assign=TypeAssign(
                                annotations=[
                                    Annotation(
                                        items=[
                                            FnCallExpr(
                                                fn_name=SimplePath(
                                                    parts=[
                                                        Ident(
                                                            symbol=Token(
                                                                "__ANON_16", "derive"
                                                            )
                                                        )
                                                    ]
                                                ),
                                                args=[
                                                    Ident(
                                                        symbol=Token(
                                                            "__ANON_16", "Sata"
                                                        )
                                                    ),
                                                    Ident(
                                                        symbol=Token(
                                                            "__ANON_16", "ansdf"
                                                        )
                                                    ),
                                                ],
                                            )
                                        ]
                                    )
                                ],
                                name=Ident(symbol=Token("__ANON_16", "token")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_16", "Addr"))
                                ),
                            ),
                            value=Ident(symbol=Token("__ANON_16", "token")),
                        ),
                        TypeAssignAndSet(
                            type_assign=TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_16", "balance")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_16", "Uint128"))
                                ),
                            ),
                            value=TableLookupExpr(
                                item=TableLookupExpr(
                                    item=TableLookupExpr(
                                        item=MemberAccessExpr(
                                            item=Ident(
                                                symbol=Token("__ANON_21", "$state")
                                            ),
                                            member=Ident(
                                                symbol=Token(
                                                    "__ANON_16", "token_balances"
                                                )
                                            ),
                                        ),
                                        key=Ident(symbol=Token("__ANON_16", "user")),
                                    ),
                                    key=Ident(symbol=Token("__ANON_16", "token")),
                                ),
                                key=Integer(value=Token("__ANON_23", "1")),
                            ),
                        ),
                    ],
                ),
                QueryDefnFn(
                    annotations=None,
                    name=Ident(symbol=Token("__ANON_16", "user_balance_for_token")),
                    args=[
                        TypeAssign(
                            annotations=None,
                            name=Ident(symbol=Token("__ANON_16", "user")),
                            type=Typename(
                                name=Ident(symbol=Token("__ANON_16", "Addr"))
                            ),
                        ),
                        TypeAssign(
                            annotations=None,
                            name=Ident(symbol=Token("__ANON_16", "token")),
                            type=Typename(
                                name=Ident(symbol=Token("__ANON_16", "Addr"))
                            ),
                        ),
                    ],
                    response_type=StructCDefn(
                        annotations=None,
                        name=Ident(
                            symbol=Token("__ANON_17", "UserBalanceForTokenResponse")
                        ),
                        members=[
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_16", "balance")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_16", "Uint128"))
                                ),
                            )
                        ],
                    ),
                    body=[
                        StructVal(
                            name=Ident(
                                symbol=Token("__ANON_17", "UserBalanceForTokenResponse")
                            ),
                            members=[
                                StructValAssign(
                                    name=Ident(symbol=Token("__ANON_16", "balance")),
                                    value=TableLookupExpr(
                                        item=TableLookupExpr(
                                            item=TableLookupExpr(
                                                item=MemberAccessExpr(
                                                    item=Ident(
                                                        symbol=Token(
                                                            "__ANON_21", "$state"
                                                        )
                                                    ),
                                                    member=Ident(
                                                        symbol=Token(
                                                            "__ANON_16",
                                                            "token_balances",
                                                        )
                                                    ),
                                                ),
                                                key=Ident(
                                                    symbol=Token("__ANON_16", "user")
                                                ),
                                            ),
                                            key=Ident(
                                                symbol=Token("__ANON_16", "token")
                                            ),
                                        ),
                                        key=Integer(value=Token("__ANON_23", "1")),
                                    ),
                                )
                            ],
                        )
                    ],
                ),
            ],
        )
    ]
)
