Module(
  body=[
    Expr(
      value=BinOp(
        left=Name(id='x', ctx=Load()),
        op=Add(),
        right=BinOp(
          left=Name(id='y', ctx=Load()),
          op=FloorDiv(),
          right=Constant(value=3))))],
  type_ignores=[])
