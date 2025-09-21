test = {
  'name': 'return-and-print',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def welcome():
          ...     print('Go')
          ...     return 'hello'
          >>> def cal():
          ...     print('Bears')
          ...     return 'world'
          >>> welcome()
          Go
          'hello'
          # locked
          >>> print(welcome(), cal())
          'hello' 
          'world'
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
