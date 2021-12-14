FileCode(
    body=[
        InterfaceDefn(
            annotations=None,
            name=Ident(symbol=Token("__ANON_21", "CW20")),
            body=[
                [
                    ExecDefn(
                        annotations=None,
                        name=Ident(symbol=Token("__ANON_20", "transfer")),
                        args=[
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_20", "recipient")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "Addr"))
                                ),
                                checks=None,
                            ),
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_20", "amount")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "Uint128"))
                                ),
                                checks=None,
                            ),
                        ],
                        body=None,
                    ),
                    ExecDefn(
                        annotations=None,
                        name=Ident(symbol=Token("__ANON_20", "send")),
                        args=[
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_20", "contract")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "Addr"))
                                ),
                                checks=None,
                            ),
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_20", "amount")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "Addr"))
                                ),
                                checks=None,
                            ),
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_20", "msg")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "Msg"))
                                ),
                                checks=None,
                            ),
                        ],
                        body=None,
                    ),
                    ExecDefn(
                        annotations=None,
                        name=Ident(symbol=Token("__ANON_20", "increase_allowance")),
                        args=[
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_20", "spender")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "Addr"))
                                ),
                                checks=None,
                            ),
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_20", "amount")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "Uint128"))
                                ),
                                checks=None,
                            ),
                            TypeAssign(
                                annotations=None,
                                name=OptionIdent(
                                    ident=Ident(symbol=Token("__ANON_20", "expires"))
                                ),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "Expiration"))
                                ),
                                checks=None,
                            ),
                        ],
                        body=None,
                    ),
                    ExecDefn(
                        annotations=None,
                        name=Ident(symbol=Token("__ANON_20", "decrease_allowance")),
                        args=[
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_20", "spender")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "Addr"))
                                ),
                                checks=None,
                            ),
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_20", "amount")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "Uint128"))
                                ),
                                checks=None,
                            ),
                            TypeAssign(
                                annotations=None,
                                name=OptionIdent(
                                    ident=Ident(symbol=Token("__ANON_20", "expires"))
                                ),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "Expiration"))
                                ),
                                checks=None,
                            ),
                        ],
                        body=None,
                    ),
                    ExecDefn(
                        annotations=None,
                        name=Ident(symbol=Token("__ANON_20", "transfer_from")),
                        args=[
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_20", "owner")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "Addr"))
                                ),
                                checks=None,
                            ),
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_20", "recipient")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "Addr"))
                                ),
                                checks=None,
                            ),
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_20", "amount")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "Uint128"))
                                ),
                                checks=None,
                            ),
                        ],
                        body=None,
                    ),
                    ExecDefn(
                        annotations=None,
                        name=Ident(symbol=Token("__ANON_20", "send_from")),
                        args=[
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_20", "owner")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "Addr"))
                                ),
                                checks=None,
                            ),
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_20", "contract")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "Addr"))
                                ),
                                checks=None,
                            ),
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_20", "amount")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "Uint128"))
                                ),
                                checks=None,
                            ),
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_20", "msg")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "Binary"))
                                ),
                                checks=None,
                            ),
                        ],
                        body=None,
                    ),
                    ExecDefn(
                        annotations=None,
                        name=Ident(symbol=Token("__ANON_20", "burn_from")),
                        args=[
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_20", "owner")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "Addr"))
                                ),
                                checks=None,
                            ),
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_20", "amount")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "Uint128"))
                                ),
                                checks=None,
                            ),
                        ],
                        body=None,
                    ),
                    ExecDefn(
                        annotations=None,
                        name=Ident(symbol=Token("__ANON_20", "mint")),
                        args=[
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_20", "recipient")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "String"))
                                ),
                                checks=None,
                            ),
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_20", "amount")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "Uint128"))
                                ),
                                checks=None,
                            ),
                        ],
                        body=None,
                    ),
                ],
                [
                    QueryDefnResponds(
                        annotations=None,
                        name=Ident(symbol=Token("__ANON_20", "balance")),
                        args=[
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_20", "address")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "Addr"))
                                ),
                                checks=None,
                            )
                        ],
                        response_defn=[
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_20", "balance")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "Uint128"))
                                ),
                                checks=None,
                            )
                        ],
                    ),
                    QueryDefnResponds(
                        annotations=None,
                        name=Ident(symbol=Token("__ANON_20", "token_info")),
                        args=[],
                        response_defn=[
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_20", "name")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "String"))
                                ),
                                checks=None,
                            ),
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_20", "symbol")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "String"))
                                ),
                                checks=None,
                            ),
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_20", "decimals")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "u8"))
                                ),
                                checks=None,
                            ),
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_20", "total_supply")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "Uint128"))
                                ),
                                checks=None,
                            ),
                        ],
                    ),
                    QueryDefnResponds(
                        annotations=None,
                        name=Ident(symbol=Token("__ANON_20", "allowance")),
                        args=[
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_20", "owner")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "String"))
                                ),
                                checks=None,
                            ),
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_20", "spender")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "String"))
                                ),
                                checks=None,
                            ),
                        ],
                        response_defn=[
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_20", "allowance")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "Uint128"))
                                ),
                                checks=None,
                            ),
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_20", "expires")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "Expiration"))
                                ),
                                checks=None,
                            ),
                        ],
                    ),
                    QueryDefnResponds(
                        annotations=None,
                        name=Ident(symbol=Token("__ANON_20", "minter")),
                        args=[],
                        response_defn=[
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_20", "minter")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "Addr"))
                                ),
                                checks=None,
                            ),
                            TypeAssign(
                                annotations=None,
                                name=OptionIdent(
                                    ident=Ident(symbol=Token("__ANON_20", "cap"))
                                ),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "Uint128"))
                                ),
                                checks=None,
                            ),
                        ],
                    ),
                    QueryDefnResponds(
                        annotations=None,
                        name=Ident(symbol=Token("__ANON_20", "marketing_info")),
                        args=[],
                        response_defn=[
                            TypeAssign(
                                annotations=None,
                                name=OptionIdent(
                                    ident=Ident(symbol=Token("__ANON_20", "project"))
                                ),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "String"))
                                ),
                                checks=None,
                            ),
                            TypeAssign(
                                annotations=None,
                                name=OptionIdent(
                                    ident=Ident(
                                        symbol=Token("__ANON_20", "description")
                                    )
                                ),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "String"))
                                ),
                                checks=None,
                            ),
                            TypeAssign(
                                annotations=None,
                                name=OptionIdent(
                                    ident=Ident(symbol=Token("__ANON_20", "logo"))
                                ),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "LogoInfo"))
                                ),
                                checks=None,
                            ),
                            TypeAssign(
                                annotations=None,
                                name=OptionIdent(
                                    ident=Ident(symbol=Token("__ANON_20", "marketing"))
                                ),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "Addr"))
                                ),
                                checks=None,
                            ),
                        ],
                    ),
                    QueryDefnResponds(
                        annotations=None,
                        name=Ident(symbol=Token("__ANON_20", "all_allowances")),
                        args=[
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_20", "owner")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "Addr"))
                                ),
                                checks=None,
                            ),
                            TypeAssign(
                                annotations=None,
                                name=OptionIdent(
                                    ident=Ident(
                                        symbol=Token("__ANON_20", "start_after")
                                    )
                                ),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "Addr"))
                                ),
                                checks=None,
                            ),
                            TypeAssign(
                                annotations=None,
                                name=OptionIdent(
                                    ident=Ident(symbol=Token("__ANON_20", "limit"))
                                ),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "u32"))
                                ),
                                checks=None,
                            ),
                        ],
                        response_defn=[
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_20", "allowances")),
                                type=VectorType(
                                    item=Typename(
                                        name=Ident(
                                            symbol=Token("__ANON_20", "AllowanceInfo")
                                        )
                                    )
                                ),
                                checks=None,
                            )
                        ],
                    ),
                    QueryDefnResponds(
                        annotations=None,
                        name=Ident(symbol=Token("__ANON_20", "all_accounts")),
                        args=[
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_20", "owner")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "Addr"))
                                ),
                                checks=None,
                            ),
                            TypeAssign(
                                annotations=None,
                                name=OptionIdent(
                                    ident=Ident(
                                        symbol=Token("__ANON_20", "start_after")
                                    )
                                ),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "Addr"))
                                ),
                                checks=None,
                            ),
                            TypeAssign(
                                annotations=None,
                                name=OptionIdent(
                                    ident=Ident(symbol=Token("__ANON_20", "limit"))
                                ),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "u32"))
                                ),
                                checks=None,
                            ),
                        ],
                        response_defn=[
                            TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_20", "accounts")),
                                type=VectorType(
                                    item=Typename(
                                        name=Ident(symbol=Token("__ANON_20", "Addr"))
                                    )
                                ),
                                checks=None,
                            )
                        ],
                    ),
                ],
            ],
        ),
        ContractDefn(
            annotations=None,
            name=Ident(symbol=Token("__ANON_21", "CW20Base")),
            parents=None,
            interfaces=[Ident(symbol=Token("__ANON_20", "CW20"))],
            body=[
                ErrorDefn(
                    annotations=None,
                    defn=EnumVariantUnit(
                        name=Ident(symbol=Token("__ANON_21", "InvalidZeroAmount"))
                    ),
                ),
                EventDefn(
                    annotations=None,
                    defn=EnumVariantStruct(
                        name=Ident(symbol=Token("__ANON_21", "Transfer")), members=[]
                    ),
                ),
                EventDefn(
                    annotations=None,
                    defn=EnumVariantStruct(
                        name=Ident(symbol=Token("__ANON_21", "Burn")), members=[]
                    ),
                ),
                EventDefn(
                    annotations=None,
                    defn=EnumVariantStruct(
                        name=Ident(symbol=Token("__ANON_21", "Mint")), members=[]
                    ),
                ),
                EventDefn(
                    annotations=None,
                    defn=EnumVariantStruct(
                        name=Ident(symbol=Token("__ANON_21", "Send")), members=[]
                    ),
                ),
                ItemDefn(
                    annotations=None,
                    key=Ident(symbol=Token("__ANON_20", "token_info")),
                    type=ReflectiveTypePath(
                        type_path=TypePath(
                            parts=[
                                Typename(name=Ident(symbol=Token("__ANON_20", "CW20"))),
                                Typename(
                                    name=Ident(symbol=Token("__ANON_20", "structs"))
                                ),
                                Typename(
                                    name=Ident(symbol=Token("__ANON_20", "TokenInfo"))
                                ),
                            ]
                        )
                    ),
                ),
                MapDefn(
                    annotations=None,
                    prefix=Ident(symbol=Token("__ANON_20", "balances")),
                    keys=[
                        MapKey(
                            key=Ident(symbol=Token("__ANON_20", "user")),
                            type=Typename(
                                name=Ident(symbol=Token("__ANON_20", "Addr"))
                            ),
                        )
                    ],
                    value=Typename(name=Ident(symbol=Token("__ANON_20", "Uint128"))),
                ),
                InstantiateDefn(
                    annotations=None,
                    args=[
                        TypeAssign(
                            annotations=None,
                            name=Ident(symbol=Token("__ANON_20", "name")),
                            type=Typename(
                                name=Ident(symbol=Token("__ANON_20", "String"))
                            ),
                            checks=None,
                        ),
                        TypeAssign(
                            annotations=None,
                            name=Ident(symbol=Token("__ANON_20", "symbol")),
                            type=Typename(
                                name=Ident(symbol=Token("__ANON_20", "String"))
                            ),
                            checks=None,
                        ),
                        TypeAssign(
                            annotations=None,
                            name=Ident(symbol=Token("__ANON_20", "decimals")),
                            type=Typename(name=Ident(symbol=Token("__ANON_20", "u8"))),
                            checks=None,
                        ),
                        TypeAssign(
                            annotations=None,
                            name=Ident(symbol=Token("__ANON_20", "initial_balances")),
                            type=VectorType(
                                item=StructCDefn(
                                    annotations=None,
                                    name=Ident(symbol=Token("__ANON_21", "Cw20Coin")),
                                    members=[
                                        TypeAssign(
                                            annotations=None,
                                            name=Ident(
                                                symbol=Token("__ANON_20", "address")
                                            ),
                                            type=Typename(
                                                name=Ident(
                                                    symbol=Token("__ANON_20", "Addr")
                                                )
                                            ),
                                            checks=None,
                                        ),
                                        TypeAssign(
                                            annotations=None,
                                            name=Ident(
                                                symbol=Token("__ANON_20", "amount")
                                            ),
                                            type=Typename(
                                                name=Ident(
                                                    symbol=Token("__ANON_20", "Uint128")
                                                )
                                            ),
                                            checks=None,
                                        ),
                                    ],
                                )
                            ),
                            checks=None,
                        ),
                        TypeAssign(
                            annotations=None,
                            name=OptionIdent(
                                ident=Ident(symbol=Token("__ANON_20", "mint"))
                            ),
                            type=ReflectiveTypePath(
                                type_path=TypePath(
                                    parts=[
                                        Typename(
                                            name=Ident(
                                                symbol=Token("__ANON_20", "CW20")
                                            )
                                        ),
                                        Typename(
                                            name=Ident(
                                                symbol=Token("__ANON_20", "query")
                                            )
                                        ),
                                        Typename(
                                            name=Ident(
                                                symbol=Token("__ANON_20", "mint")
                                            )
                                        ),
                                        Typename(
                                            name=Ident(
                                                symbol=Token("__ANON_20", "response")
                                            )
                                        ),
                                    ]
                                )
                            ),
                            checks=None,
                        ),
                    ],
                    body=[
                        AssignStmt(
                            lhs=Ident(symbol=Token("__ANON_20", "total_supply")),
                            assign_op=Token("EQUAL", "="),
                            rhs=FnCallExpr(
                                fn_name=Ident(symbol=Token("__ANON_20", "Uint128")),
                                args=[Integer(value=Token("__ANON_25", "0"))],
                            ),
                        ),
                        ForStmt(
                            for_elems=ForDestructure(
                                idents=[
                                    Ident(symbol=Token("__ANON_20", "address")),
                                    Ident(symbol=Token("__ANON_20", "amount")),
                                ]
                            ),
                            iterable=Ident(
                                symbol=Token("__ANON_20", "initial_balances")
                            ),
                            body=[
                                TableLookupExpr(
                                    item=MemberAccessExpr(
                                        item=Ident(symbol=Token("__ANON_20", "$state")),
                                        member=Ident(
                                            symbol=Token("__ANON_20", "balances")
                                        ),
                                    ),
                                    key=Ident(symbol=Token("__ANON_20", "address")),
                                ),
                                AssignStmt(
                                    lhs=Ident(
                                        symbol=Token("__ANON_20", "total_supply")
                                    ),
                                    assign_op=Token("__ANON_6", "+="),
                                    rhs=Ident(symbol=Token("__ANON_20", "amount")),
                                ),
                            ],
                        ),
                        AssignStmt(
                            lhs=MemberAccessExpr(
                                item=Ident(symbol=Token("__ANON_20", "$state")),
                                member=Ident(symbol=Token("__ANON_20", "token_info")),
                            ),
                            assign_op=Token("EQUAL", "="),
                            rhs=StructVal(
                                name=Ident(symbol=Token("__ANON_21", "TokenInfo")),
                                members=[
                                    StructValAssign(
                                        name=Ident(symbol=Token("__ANON_20", "name")),
                                        value=Ident(symbol=Token("__ANON_20", "name")),
                                    ),
                                    StructValAssign(
                                        name=Ident(symbol=Token("__ANON_20", "symbol")),
                                        value=Ident(
                                            symbol=Token("__ANON_20", "symbol")
                                        ),
                                    ),
                                    StructValAssign(
                                        name=Ident(
                                            symbol=Token("__ANON_20", "decimals")
                                        ),
                                        value=Ident(
                                            symbol=Token("__ANON_20", "decimals")
                                        ),
                                    ),
                                    StructValAssign(
                                        name=Ident(
                                            symbol=Token("__ANON_20", "total_supply")
                                        ),
                                        value=Ident(
                                            symbol=Token("__ANON_20", "total_supply")
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
                CheckLambda(
                    name=Ident(symbol=Token("__ANON_20", "not0")),
                    type_bound=None,
                    predicate=InfixOpExpr(
                        lhs=Ident(symbol=Token("__ANON_20", "$arg")),
                        op=Token("__ANON_15", "=="),
                        rhs=Integer(value=Token("__ANON_25", "0")),
                    ),
                    error_type=Ident(symbol=Token("__ANON_20", "InvalidZeroAmount")),
                ),
                CheckFn(
                    name=Ident(symbol=Token("__ANON_20", "not0")),
                    type_bound=None,
                    body=[
                        IfExpr(
                            if_clause=IfClause(
                                predicate=InfixOpExpr(
                                    lhs=Ident(symbol=Token("__ANON_20", "$arg")),
                                    op=Token("__ANON_15", "=="),
                                    rhs=Integer(value=Token("__ANON_25", "0")),
                                ),
                                body=[
                                    FailStmt(
                                        expr=Ident(
                                            symbol=Token(
                                                "__ANON_20", "InvalidZeroAmount"
                                            )
                                        )
                                    )
                                ],
                            ),
                            else_if_clauses=None,
                            else_body=None,
                        )
                    ],
                ),
                CheckLambda(
                    name=Ident(symbol=Token("__ANON_20", "valid")),
                    type_bound=Typename(name=Ident(symbol=Token("__ANON_20", "Addr"))),
                    predicate=FnCallExpr(
                        fn_name=MemberAccessExpr(
                            item=Ident(symbol=Token("__ANON_20", "$api")),
                            member=Ident(symbol=Token("__ANON_20", "addr_validate")),
                        ),
                        args=[Ident(symbol=Token("__ANON_20", "$arg"))],
                    ),
                    error_type=None,
                ),
                ExecDefn(
                    annotations=None,
                    name=Ident(symbol=Token("__ANON_20", "transfer")),
                    args=[
                        TypeAssign(
                            annotations=None,
                            name=Ident(symbol=Token("__ANON_20", "recipient")),
                            type=Typename(
                                name=Ident(symbol=Token("__ANON_20", "Addr"))
                            ),
                            checks=None,
                        ),
                        TypeAssign(
                            annotations=None,
                            name=Ident(symbol=Token("__ANON_20", "amount")),
                            type=Typename(
                                name=Ident(symbol=Token("__ANON_20", "Uint128"))
                            ),
                            checks=[
                                Check(
                                    name=Ident(symbol=Token("__ANON_20", "not0")),
                                    args=None,
                                )
                            ],
                        ),
                    ],
                    body=[
                        AssignStmt(
                            lhs=TableLookupExpr(
                                item=MemberAccessExpr(
                                    item=Ident(symbol=Token("__ANON_20", "$state")),
                                    member=Ident(symbol=Token("__ANON_20", "balances")),
                                ),
                                key=MemberAccessExpr(
                                    item=Ident(symbol=Token("__ANON_20", "$msg")),
                                    member=Ident(symbol=Token("__ANON_20", "sender")),
                                ),
                            ),
                            assign_op=Token("__ANON_7", "-="),
                            rhs=Ident(symbol=Token("__ANON_20", "amount")),
                        ),
                        AssignStmt(
                            lhs=TableLookupExpr(
                                item=MemberAccessExpr(
                                    item=Ident(symbol=Token("__ANON_20", "$state")),
                                    member=Ident(symbol=Token("__ANON_20", "balances")),
                                ),
                                key=Ident(symbol=Token("__ANON_20", "recipient")),
                            ),
                            assign_op=Token("__ANON_6", "+="),
                            rhs=Ident(symbol=Token("__ANON_20", "amount")),
                        ),
                        EmitStmt(
                            expr=FnCallExpr(
                                fn_name=Ident(symbol=Token("__ANON_20", "Transfer")),
                                args=[
                                    MemberAccessExpr(
                                        item=Ident(symbol=Token("__ANON_20", "$msg")),
                                        member=Ident(
                                            symbol=Token("__ANON_20", "sender")
                                        ),
                                    ),
                                    Ident(symbol=Token("__ANON_20", "recipient")),
                                    Ident(symbol=Token("__ANON_20", "amount")),
                                ],
                            )
                        ),
                    ],
                ),
                ExecDefn(
                    annotations=None,
                    name=Ident(symbol=Token("__ANON_20", "burn")),
                    args=[
                        TypeAssign(
                            annotations=None,
                            name=Ident(symbol=Token("__ANON_20", "amount")),
                            type=Typename(
                                name=Ident(symbol=Token("__ANON_20", "Uint128"))
                            ),
                            checks=[
                                Check(
                                    name=Ident(symbol=Token("__ANON_20", "not0")),
                                    args=None,
                                )
                            ],
                        )
                    ],
                    body=[
                        AssignStmt(
                            lhs=TableLookupExpr(
                                item=MemberAccessExpr(
                                    item=Ident(symbol=Token("__ANON_20", "$state")),
                                    member=Ident(symbol=Token("__ANON_20", "balances")),
                                ),
                                key=MemberAccessExpr(
                                    item=Ident(symbol=Token("__ANON_20", "$info")),
                                    member=Ident(symbol=Token("__ANON_20", "sender")),
                                ),
                            ),
                            assign_op=Token("__ANON_7", "-="),
                            rhs=Ident(symbol=Token("__ANON_20", "amount")),
                        ),
                        AssignStmt(
                            lhs=MemberAccessExpr(
                                item=Ident(symbol=Token("__ANON_20", "$state")),
                                member=Ident(symbol=Token("__ANON_20", "token_supply")),
                            ),
                            assign_op=Token("__ANON_7", "-="),
                            rhs=Ident(symbol=Token("__ANON_20", "amount")),
                        ),
                        EmitStmt(
                            expr=FnCallExpr(
                                fn_name=Ident(symbol=Token("__ANON_20", "Burn")),
                                args=[
                                    MemberAccessExpr(
                                        item=Ident(symbol=Token("__ANON_20", "$info")),
                                        member=Ident(
                                            symbol=Token("__ANON_20", "sender")
                                        ),
                                    ),
                                    Ident(symbol=Token("__ANON_20", "amount")),
                                ],
                            )
                        ),
                    ],
                ),
                ExecDefn(
                    annotations=None,
                    name=Ident(symbol=Token("__ANON_20", "mint")),
                    args=[
                        TypeAssign(
                            annotations=None,
                            name=Ident(symbol=Token("__ANON_20", "recipient")),
                            type=Typename(
                                name=Ident(symbol=Token("__ANON_20", "Addr"))
                            ),
                            checks=[
                                Check(
                                    name=Ident(symbol=Token("__ANON_20", "valid")),
                                    args=None,
                                )
                            ],
                        ),
                        TypeAssign(
                            annotations=None,
                            name=Ident(symbol=Token("__ANON_20", "amount")),
                            type=Typename(
                                name=Ident(symbol=Token("__ANON_20", "Uint128"))
                            ),
                            checks=[
                                Check(
                                    name=Ident(symbol=Token("__ANON_20", "not0")),
                                    args=[Integer(value=Token("__ANON_25", "0"))],
                                ),
                                Check(
                                    name=Ident(symbol=Token("__ANON_20", "item0")),
                                    args=None,
                                ),
                            ],
                        ),
                    ],
                    body=[
                        AssignStmt(
                            lhs=Ident(symbol=Token("__ANON_20", "config")),
                            assign_op=Token("EQUAL", "="),
                            rhs=MemberAccessExpr(
                                item=Ident(symbol=Token("__ANON_20", "$state")),
                                member=Ident(symbol=Token("__ANON_20", "token_info")),
                            ),
                        ),
                        IfExpr(
                            if_clause=IfClause(
                                predicate=OrExpr(
                                    a=InfixOpExpr(
                                        lhs=MemberAccessExpr(
                                            item=Ident(
                                                symbol=Token("__ANON_20", "config")
                                            ),
                                            member=Ident(
                                                symbol=Token("__ANON_20", "mint")
                                            ),
                                        ),
                                        op=Token("__ANON_15", "=="),
                                        rhs=Ident(symbol=Token("__ANON_20", "None")),
                                    ),
                                    b=MemberAccessExpr(
                                        item=InfixOpExpr(
                                            lhs=MemberAccessExpr(
                                                item=MemberAccessExpr(
                                                    item=Ident(
                                                        symbol=Token(
                                                            "__ANON_20", "config"
                                                        )
                                                    ),
                                                    member=Ident(
                                                        symbol=Token(
                                                            "__ANON_20", "mint"
                                                        )
                                                    ),
                                                ),
                                                member=Ident(
                                                    symbol=Token("__ANON_20", "minter")
                                                ),
                                            ),
                                            op=Token("__ANON_16", "!="),
                                            rhs=Ident(
                                                symbol=Token("__ANON_20", "$msg")
                                            ),
                                        ),
                                        member=Ident(
                                            symbol=Token("__ANON_20", "sender")
                                        ),
                                    ),
                                ),
                                body=[
                                    FailStmt(
                                        expr=Ident(
                                            symbol=Token("__ANON_20", "Unauthorized")
                                        )
                                    )
                                ],
                            ),
                            else_if_clauses=None,
                            else_body=None,
                        ),
                        AssignStmt(
                            lhs=MemberAccessExpr(
                                item=Ident(symbol=Token("__ANON_20", "config")),
                                member=Ident(symbol=Token("__ANON_20", "total_supply")),
                            ),
                            assign_op=Token("__ANON_6", "+="),
                            rhs=Ident(symbol=Token("__ANON_20", "amount")),
                        ),
                        IfExpr(
                            if_clause=IfSome(
                                predicate=AndExpr(
                                    a=IdentAssignExpr(
                                        ident=Ident(symbol=Token("__ANON_20", "limit")),
                                        val=FnCallExpr(
                                            fn_name=MemberAccessExpr(
                                                item=Ident(
                                                    symbol=Token("__ANON_20", "config")
                                                ),
                                                member=Ident(
                                                    symbol=Token("__ANON_20", "get_cap")
                                                ),
                                            ),
                                            args=[],
                                        ),
                                    ),
                                    b=InfixOpExpr(
                                        lhs=MemberAccessExpr(
                                            item=Ident(
                                                symbol=Token("__ANON_20", "config")
                                            ),
                                            member=Ident(
                                                symbol=Token(
                                                    "__ANON_20", "total_supply"
                                                )
                                            ),
                                        ),
                                        op=Token("MORETHAN", ">"),
                                        rhs=Ident(symbol=Token("__ANON_20", "limit")),
                                    ),
                                ),
                                body=[
                                    FailStmt(
                                        expr=Ident(
                                            symbol=Token("__ANON_20", "CannotExceedCap")
                                        )
                                    )
                                ],
                            ),
                            else_if_clauses=None,
                            else_body=None,
                        ),
                        AssignStmt(
                            lhs=MemberAccessExpr(
                                item=Ident(symbol=Token("__ANON_20", "$state")),
                                member=Ident(symbol=Token("__ANON_20", "token_info")),
                            ),
                            assign_op=Token("EQUAL", "="),
                            rhs=Ident(symbol=Token("__ANON_20", "config")),
                        ),
                        AssignStmt(
                            lhs=TableLookupExpr(
                                item=MemberAccessExpr(
                                    item=Ident(symbol=Token("__ANON_20", "$state")),
                                    member=Ident(symbol=Token("__ANON_20", "balances")),
                                ),
                                key=Ident(symbol=Token("__ANON_20", "recipient")),
                            ),
                            assign_op=Token("__ANON_6", "+="),
                            rhs=Ident(symbol=Token("__ANON_20", "amount")),
                        ),
                        EmitStmt(
                            expr=FnCallExpr(
                                fn_name=Ident(symbol=Token("__ANON_20", "Mint")),
                                args=[
                                    Ident(symbol=Token("__ANON_20", "recipient")),
                                    Ident(symbol=Token("__ANON_20", "amount")),
                                ],
                            )
                        ),
                    ],
                ),
                ExecDefn(
                    annotations=None,
                    name=Ident(symbol=Token("__ANON_20", "send")),
                    args=[
                        TypeAssign(
                            annotations=None,
                            name=Ident(symbol=Token("__ANON_20", "contract")),
                            type=Typename(
                                name=Ident(symbol=Token("__ANON_20", "Addr"))
                            ),
                            checks=[
                                Check(
                                    name=Ident(symbol=Token("__ANON_20", "valid")),
                                    args=None,
                                )
                            ],
                        ),
                        TypeAssign(
                            annotations=None,
                            name=Ident(symbol=Token("__ANON_20", "amount")),
                            type=Typename(
                                name=Ident(symbol=Token("__ANON_20", "Uint128"))
                            ),
                            checks=[
                                Check(
                                    name=Ident(symbol=Token("__ANON_20", "non0")),
                                    args=None,
                                )
                            ],
                        ),
                        TypeAssign(
                            annotations=None,
                            name=Ident(symbol=Token("__ANON_20", "msg")),
                            type=Typename(
                                name=Ident(symbol=Token("__ANON_20", "Binary"))
                            ),
                            checks=None,
                        ),
                    ],
                    body=[
                        AssignStmt(
                            lhs=TableLookupExpr(
                                item=MemberAccessExpr(
                                    item=Ident(symbol=Token("__ANON_20", "$state")),
                                    member=Ident(symbol=Token("__ANON_20", "balances")),
                                ),
                                key=MemberAccessExpr(
                                    item=Ident(symbol=Token("__ANON_20", "$msg")),
                                    member=Ident(symbol=Token("__ANON_20", "sender")),
                                ),
                            ),
                            assign_op=Token("__ANON_7", "-="),
                            rhs=Ident(symbol=Token("__ANON_20", "amount")),
                        ),
                        AssignStmt(
                            lhs=TableLookupExpr(
                                item=MemberAccessExpr(
                                    item=Ident(symbol=Token("__ANON_20", "$state")),
                                    member=Ident(symbol=Token("__ANON_20", "balances")),
                                ),
                                key=Ident(symbol=Token("__ANON_20", "contract")),
                            ),
                            assign_op=Token("__ANON_6", "+="),
                            rhs=Ident(symbol=Token("__ANON_20", "amount")),
                        ),
                        EmitStmt(
                            expr=FnCallExpr(
                                fn_name=Ident(symbol=Token("__ANON_20", "Send")),
                                args=[
                                    MemberAccessExpr(
                                        item=Ident(symbol=Token("__ANON_20", "$msg")),
                                        member=Ident(
                                            symbol=Token("__ANON_20", "sender")
                                        ),
                                    ),
                                    Ident(symbol=Token("__ANON_20", "contract")),
                                    Ident(symbol=Token("__ANON_20", "amount")),
                                ],
                            )
                        ),
                        Tree(
                            "exec_stmt",
                            [
                                StructCallExpr(
                                    fn=MemberAccessExpr(
                                        item=FnCallExpr(
                                            fn_name=Ident(
                                                symbol=Token(
                                                    "__ANON_20", "CW20Receiver"
                                                )
                                            ),
                                            args=[
                                                Ident(
                                                    symbol=Token(
                                                        "__ANON_20", "contract"
                                                    )
                                                )
                                            ],
                                        ),
                                        member=Ident(
                                            symbol=Token("__ANON_20", "receive")
                                        ),
                                    ),
                                    args=[
                                        StructArg(
                                            name=Ident(
                                                symbol=Token("__ANON_20", "sender")
                                            ),
                                            value=MemberAccessExpr(
                                                item=Ident(
                                                    symbol=Token("__ANON_20", "$msg")
                                                ),
                                                member=Ident(
                                                    symbol=Token("__ANON_20", "sender")
                                                ),
                                            ),
                                        ),
                                        StructArg(
                                            name=None,
                                            value=Ident(
                                                symbol=Token("__ANON_20", "amount")
                                            ),
                                        ),
                                        StructArg(
                                            name=None,
                                            value=Ident(
                                                symbol=Token("__ANON_20", "msg")
                                            ),
                                        ),
                                    ],
                                )
                            ],
                        ),
                    ],
                ),
                QueryDefnResponds(
                    annotations=None,
                    name=Ident(symbol=Token("__ANON_20", "balance")),
                    args=[
                        TypeAssign(
                            annotations=None,
                            name=Ident(symbol=Token("__ANON_20", "address")),
                            type=Typename(
                                name=Ident(symbol=Token("__ANON_20", "Addr"))
                            ),
                            checks=[
                                Check(
                                    name=Ident(symbol=Token("__ANON_20", "valid")),
                                    args=None,
                                )
                            ],
                        )
                    ],
                    response_defn=[
                        TypeAssignAndSet(
                            type_assign=TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_20", "balance")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "Uint128"))
                                ),
                                checks=None,
                            ),
                            value=OrExpr(
                                a=TableLookupExpr(
                                    item=MemberAccessExpr(
                                        item=Ident(symbol=Token("__ANON_20", "$state")),
                                        member=Ident(
                                            symbol=Token("__ANON_20", "balances")
                                        ),
                                    ),
                                    key=Ident(symbol=Token("__ANON_20", "address")),
                                ),
                                b=Integer(value=Token("__ANON_25", "0")),
                            ),
                        )
                    ],
                ),
                QueryDefnResponds(
                    annotations=None,
                    name=Ident(symbol=Token("__ANON_20", "token_info")),
                    args=[],
                    response_defn=[
                        TypeAssignAndSet(
                            type_assign=TypeAssign(
                                annotations=None,
                                name=Ident(symbol=Token("__ANON_20", "token_info")),
                                type=Typename(
                                    name=Ident(symbol=Token("__ANON_20", "TokenInfo"))
                                ),
                                checks=None,
                            ),
                            value=MemberAccessExpr(
                                item=Ident(symbol=Token("__ANON_20", "$state")),
                                member=Ident(symbol=Token("__ANON_20", "token_info")),
                            ),
                        )
                    ],
                ),
                QueryDefnFn(
                    annotations=None,
                    name=Ident(symbol=Token("__ANON_20", "minter")),
                    args=[],
                    response_type=Option(
                        wrapped=ReflectiveTypePath(
                            type_path=TypePath(
                                parts=[
                                    Typename(
                                        name=Ident(symbol=Token("__ANON_20", "CW20"))
                                    ),
                                    Typename(
                                        name=Ident(symbol=Token("__ANON_20", "query"))
                                    ),
                                    Typename(
                                        name=Ident(symbol=Token("__ANON_20", "minter"))
                                    ),
                                    Typename(
                                        name=Ident(
                                            symbol=Token("__ANON_20", "response")
                                        )
                                    ),
                                ]
                            )
                        )
                    ),
                    body=[
                        AssignStmt(
                            lhs=Ident(symbol=Token("__ANON_20", "meta")),
                            assign_op=Token("EQUAL", "="),
                            rhs=MemberAccessExpr(
                                item=Ident(symbol=Token("__ANON_20", "$state")),
                                member=Ident(symbol=Token("__ANON_20", "token_info")),
                            ),
                        ),
                        IfExpr(
                            if_clause=IfSome(
                                predicate=MemberAccessExpr(
                                    item=Ident(symbol=Token("__ANON_20", "meta")),
                                    member=Ident(symbol=Token("__ANON_20", "minter")),
                                ),
                                body=[
                                    Tree(
                                        "return_stmt",
                                        [Ident(symbol=Token("__ANON_20", "minter"))],
                                    )
                                ],
                            ),
                            else_if_clauses=None,
                            else_body=[
                                Tree(
                                    "return_stmt",
                                    [Ident(symbol=Token("__ANON_20", "None"))],
                                )
                            ],
                        ),
                    ],
                ),
            ],
        ),
        ContractDefn(
            annotations=None,
            name=Ident(symbol=Token("__ANON_21", "MyToken")),
            parents=[Ident(symbol=Token("__ANON_20", "CW20Base"))],
            interfaces=None,
            body=[],
        ),
    ]
)
