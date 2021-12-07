FileCode(
    statements=[
        ContractDefn(
            name=Token("__ANON_16", "CW20"),
            body=[
                DeclError(
                    defns=[
                        ErrorDefn(
                            name=Token("__ANON_16", "ImproperFormat"),
                            members=[
                                TypeAssign(
                                    name=Token("__ANON_15", "user"),
                                    type=Typename(name=Token("__ANON_15", "Addr")),
                                ),
                                TypeAssign(
                                    name=Token("__ANON_15", "input"),
                                    type=Typename(name=Token("__ANON_15", "String")),
                                ),
                            ],
                            body=[
                                IfExpr(
                                    if_clause=IfClause(
                                        predicate=InfixOpExpr(
                                            lhs=Token("__ANON_15", "input"),
                                            op=Token("__ANON_11", "!="),
                                            rhs=Token("__ANON_15", "None"),
                                        ),
                                        body=[
                                            String(
                                                value=Token(
                                                    "ESCAPED_STRING",
                                                    '"wrong format for user, got {input}"',
                                                )
                                            )
                                        ],
                                    ),
                                    else_if_clauses=None,
                                    else_body=[
                                        String(
                                            value=Token(
                                                "ESCAPED_STRING",
                                                '"wrong format for user"',
                                            )
                                        )
                                    ],
                                )
                            ],
                        )
                    ]
                ),
                DeclError(
                    defns=[
                        ErrorDefn(
                            name=Token("__ANON_16", "NotEnabled"),
                            members=[
                                TypeAssign(
                                    name=Token("__ANON_15", "req_level"),
                                    type=DeclEnum(
                                        name=Token("__ANON_16", "Levels"),
                                        variants=[
                                            EnumVariantUnit(
                                                name=Token("__ANON_16", "Admin")
                                            ),
                                            EnumVariantUnit(
                                                name=Token("__ANON_16", "Student")
                                            ),
                                        ],
                                    ),
                                )
                            ],
                            body=[
                                IfExpr(
                                    if_clause=IfClause(
                                        predicate=InfixOpExpr(
                                            lhs=Token("__ANON_15", "req_level"),
                                            op=Token("__ANON_10", "=="),
                                            rhs=InfixOpExpr(
                                                lhs=Token("__ANON_15", "Levels"),
                                                op=Token("__ANON_14", "::"),
                                                rhs=Token("__ANON_15", "Admin"),
                                            ),
                                        ),
                                        body=[
                                            String(
                                                value=Token(
                                                    "ESCAPED_STRING",
                                                    '"you must be an admin to access this portion"',
                                                )
                                            )
                                        ],
                                    ),
                                    else_if_clauses=None,
                                    else_body=[
                                        String(
                                            value=Token(
                                                "ESCAPED_STRING",
                                                '"the required level is student, unfortunately"',
                                            )
                                        )
                                    ],
                                )
                            ],
                        ),
                        ErrorDefn(
                            name=Token("__ANON_16", "Unauthorized"),
                            members=None,
                            body=None,
                        ),
                        ErrorDefn(
                            name=Token("__ANON_16", "InsufficientFunds"),
                            members=[
                                TypeAssign(
                                    name=Token("__ANON_15", "balance"),
                                    type=Typename(name=Token("__ANON_15", "Uint128")),
                                ),
                                TypeAssign(
                                    name=Token("__ANON_15", "needed"),
                                    type=Typename(name=Token("__ANON_15", "Uint128")),
                                ),
                            ],
                            body=[
                                String(
                                    value=Token(
                                        "ESCAPED_STRING",
                                        '"you only had {balance}, which is less than the {needed} required"',
                                    )
                                )
                            ],
                        ),
                    ]
                ),
                DeclEvent(
                    defns=[
                        EventDefn(
                            name=Token("__ANON_16", "Action"),
                            members=[
                                TypeAssign(
                                    name=Token("__ANON_15", "method"),
                                    type=Typename(name=Token("__ANON_15", "String")),
                                ),
                                TypeAssign(
                                    name=Token("__ANON_15", "owner"),
                                    type=Typename(name=Token("__ANON_15", "String")),
                                ),
                                TypeAssign(
                                    name=Token("__ANON_15", "count"),
                                    type=Typename(name=Token("__ANON_15", "String")),
                                ),
                            ],
                            body=None,
                        )
                    ]
                ),
                DeclEvent(
                    defns=[
                        EventDefn(
                            name=Token("__ANON_16", "Increment"),
                            members=None,
                            body=None,
                        ),
                        EventDefn(
                            name=Token("__ANON_16", "Reset"),
                            members=[
                                TypeAssign(
                                    name=Token("__ANON_15", "method"),
                                    type=Typename(name=Token("__ANON_15", "String")),
                                )
                            ],
                            body=None,
                        ),
                    ]
                ),
                DeclState(
                    defns=[
                        ItemDefn(
                            key=Token("__ANON_15", "curr_num"),
                            type_expr=Typename(name=Token("__ANON_15", "i32")),
                        )
                    ]
                ),
                DeclState(
                    defns=[
                        MapDefn(
                            prefix=Token("__ANON_15", "balances"),
                            type_keys=[
                                MapKeyDefn(
                                    key=None,
                                    type=Typename(name=Token("__ANON_15", "Addr")),
                                )
                            ],
                            type_value=Typename(name=Token("__ANON_15", "Uint128")),
                        )
                    ]
                ),
                DeclState(
                    defns=[
                        ItemDefn(
                            key=Token("__ANON_15", "config"),
                            type_expr=StructDictDefn(
                                name=Token("__ANON_16", "ConfigData"),
                                members=[
                                    TypeAssign(
                                        name=Token("__ANON_15", "owner"),
                                        type=Typename(name=Token("__ANON_15", "Addr")),
                                    ),
                                    TypeAssign(
                                        name=Token("__ANON_15", "count"),
                                        type=Typename(name=Token("__ANON_15", "i32")),
                                    ),
                                    TypeAssign(
                                        name=Token("__ANON_15", "fee_percent"),
                                        type=Typename(
                                            name=Token("__ANON_15", "Decimal")
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        MapDefn(
                            prefix=Token("__ANON_15", "token_balances"),
                            type_keys=[
                                MapKeyDefn(
                                    key=Token("__ANON_15", "user"),
                                    type=Typename(name=Token("__ANON_15", "Addr")),
                                ),
                                MapKeyDefn(
                                    key=None,
                                    type=Typename(name=Token("__ANON_15", "Addr")),
                                ),
                                MapKeyDefn(
                                    key=Token("__ANON_15", "bucket"),
                                    type=Typename(name=Token("__ANON_15", "u32")),
                                ),
                            ],
                            type_value=Typename(name=Token("__ANON_15", "Uint128")),
                        ),
                    ]
                ),
                DeclInstantiate(
                    defn=InstantiateDefn(
                        args=[
                            TypeAssign(
                                name=Token("__ANON_15", "count"),
                                type=Typename(name=Token("__ANON_15", "i32")),
                            ),
                            TypeAssign(
                                name=Token("__ANON_15", "fee_percent"),
                                type=Typename(name=Token("__ANON_15", "Dec")),
                            ),
                        ],
                        body=[
                            AssignStmt(
                                lhs=IdentPath(
                                    parts=[
                                        Token("__ANON_15", "$state"),
                                        Token("__ANON_15", "config"),
                                    ]
                                ),
                                assign_op="=",
                                rhs=StructDictVal(
                                    name=Token("__ANON_16", "ConfigData"),
                                    members_vals=[
                                        StructDictAssign(
                                            name=Token("__ANON_15", "owner"),
                                            value=MemberAccessExpr(
                                                item=Token("__ANON_15", "$env"),
                                                member=Token("__ANON_15", "sender"),
                                            ),
                                        ),
                                        StructDictAssign(
                                            name=Token("__ANON_15", "count"),
                                            value=Token("__ANON_15", "count"),
                                        ),
                                        StructDictAssign(
                                            name=Token("__ANON_15", "fee_percent"),
                                            value=Token("__ANON_15", "fee_percent"),
                                        ),
                                    ],
                                ),
                            ),
                            EmitStmt(
                                expr=FnCallExpr(
                                    fn_name=Token("__ANON_15", "Action"),
                                    args=[
                                        String(
                                            value=Token(
                                                "ESCAPED_STRING", '"instantiate"'
                                            )
                                        ),
                                        MemberAccessExpr(
                                            item=Token("__ANON_15", "$env"),
                                            member=Token("__ANON_15", "sender"),
                                        ),
                                        Token("__ANON_15", "count"),
                                    ],
                                )
                            ),
                        ],
                    )
                ),
                DeclExec(
                    defns=[
                        ExecDefn(
                            name=Token("__ANON_15", "msg_name_snake_case"),
                            args=[
                                TypeAssign(
                                    name=Token("__ANON_15", "arg1"),
                                    type=Typename(name=Token("__ANON_15", "u32")),
                                ),
                                TypeAssign(
                                    name=Token("__ANON_15", "arg2"),
                                    type=ParamzdTypeExpr(
                                        base_type=Typename(
                                            name=Token("__ANON_15", "Option")
                                        ),
                                        param=Typename(
                                            name=Token("__ANON_15", "String")
                                        ),
                                    ),
                                ),
                            ],
                            body=[],
                        )
                    ]
                ),
                DeclExec(
                    defns=[
                        ExecDefn(
                            name=Token("__ANON_15", "increment"),
                            args=None,
                            body=[
                                AssignStmt(
                                    lhs=IdentPath(
                                        parts=[
                                            Token("__ANON_15", "$state"),
                                            Token("__ANON_15", "config"),
                                            Token("__ANON_15", "count"),
                                        ]
                                    ),
                                    assign_op="+=",
                                    rhs=Integer(value=Token("__ANON_19", "1")),
                                )
                            ],
                        ),
                        ExecDefn(
                            name=Token("__ANON_15", "reset"),
                            args=[
                                TypeAssign(
                                    name=Token("__ANON_15", "count"),
                                    type=Typename(name=Token("__ANON_15", "i32")),
                                )
                            ],
                            body=[
                                IfExpr(
                                    if_clause=IfClause(
                                        predicate=MemberAccessExpr(
                                            item=MemberAccessExpr(
                                                item=InfixOpExpr(
                                                    lhs=MemberAccessExpr(
                                                        item=Token("__ANON_15", "$env"),
                                                        member=Token(
                                                            "__ANON_15", "sender"
                                                        ),
                                                    ),
                                                    op=Token("__ANON_11", "!="),
                                                    rhs=Token("__ANON_15", "$state"),
                                                ),
                                                member=Token("__ANON_15", "config"),
                                            ),
                                            member=Token("__ANON_15", "owner"),
                                        ),
                                        body=[
                                            FailStmt(
                                                expr=Token("__ANON_15", "Unauthorized")
                                            )
                                        ],
                                    ),
                                    else_if_clauses=None,
                                    else_body=None,
                                ),
                                AssignStmt(
                                    lhs=IdentPath(
                                        parts=[
                                            Token("__ANON_15", "$state"),
                                            Token("__ANON_15", "config"),
                                            Token("__ANON_15", "count"),
                                        ]
                                    ),
                                    assign_op="=",
                                    rhs=Token("__ANON_15", "count"),
                                ),
                            ],
                        ),
                    ]
                ),
                DeclQuery(
                    defns=[
                        QueryDefnFn(
                            name=Token("__ANON_15", "count"),
                            args=None,
                            response_type=StructDictDefn(
                                name=Token("__ANON_16", "CountResponse"),
                                members=[
                                    TypeAssign(
                                        name=Token("__ANON_15", "count"),
                                        type=Typename(name=Token("__ANON_15", "i32")),
                                    )
                                ],
                            ),
                            body=[
                                StructDictVal(
                                    name=Token("__ANON_16", "CountResponse"),
                                    members_vals=StructDictAssign(
                                        name=Token("__ANON_15", "count"),
                                        value=MemberAccessExpr(
                                            item=MemberAccessExpr(
                                                item=Token("__ANON_15", "$state"),
                                                member=Token("__ANON_15", "config"),
                                            ),
                                            member=Token("__ANON_15", "count"),
                                        ),
                                    ),
                                )
                            ],
                        )
                    ]
                ),
                DeclQuery(
                    defns=[
                        QueryDefnResponds(
                            name=Token("__ANON_15", "user_balance_for_token"),
                            args=[
                                TypeAssign(
                                    name=Token("__ANON_15", "user"),
                                    type=Typename(name=Token("__ANON_15", "Addr")),
                                ),
                                TypeAssign(
                                    name=Token("__ANON_15", "token"),
                                    type=Typename(name=Token("__ANON_15", "Addr")),
                                ),
                            ],
                            response_defn=TypeAssignAndSet(
                                type_assign=TypeAssign(
                                    name=Token("__ANON_15", "balance"),
                                    type=Typename(name=Token("__ANON_15", "Uint128")),
                                ),
                                value=TableLookupExpr(
                                    item=TableLookupExpr(
                                        item=TableLookupExpr(
                                            item=MemberAccessExpr(
                                                item=Token("__ANON_15", "$state"),
                                                member=Token(
                                                    "__ANON_15", "token_balances"
                                                ),
                                            ),
                                            key=Token("__ANON_15", "user"),
                                        ),
                                        key=Token("__ANON_15", "token"),
                                    ),
                                    key=Integer(value=Token("__ANON_19", "1")),
                                ),
                            ),
                        )
                    ]
                ),
                DeclQuery(
                    defns=[
                        QueryDefnFn(
                            name=Token("__ANON_15", "user_balance_for_token"),
                            args=[
                                TypeAssign(
                                    name=Token("__ANON_15", "user"),
                                    type=Typename(name=Token("__ANON_15", "Addr")),
                                ),
                                TypeAssign(
                                    name=Token("__ANON_15", "token"),
                                    type=Typename(name=Token("__ANON_15", "Addr")),
                                ),
                            ],
                            response_type=StructDictDefn(
                                name=Token("__ANON_16", "UserBalanceForTokenResponse"),
                                members=[
                                    TypeAssign(
                                        name=Token("__ANON_15", "balance"),
                                        type=Typename(
                                            name=Token("__ANON_15", "Uint128")
                                        ),
                                    )
                                ],
                            ),
                            body=[
                                StructDictVal(
                                    name=Token(
                                        "__ANON_16", "UserBalanceForTokenResponse"
                                    ),
                                    members_vals=StructDictAssign(
                                        name=Token("__ANON_15", "balance"),
                                        value=TableLookupExpr(
                                            item=TableLookupExpr(
                                                item=TableLookupExpr(
                                                    item=MemberAccessExpr(
                                                        item=Token(
                                                            "__ANON_15", "$state"
                                                        ),
                                                        member=Token(
                                                            "__ANON_15",
                                                            "token_balances",
                                                        ),
                                                    ),
                                                    key=Token("__ANON_15", "user"),
                                                ),
                                                key=Token("__ANON_15", "token"),
                                            ),
                                            key=Integer(value=Token("__ANON_19", "1")),
                                        ),
                                    ),
                                )
                            ],
                        )
                    ]
                ),
            ],
        )
    ]
)
