# CHANGELOG

<!-- version list -->

## v0.6.2 (2025-06-16)

### Bug Fixes

- Enhance create and update methods to handle many-to-many attributes
  ([`08b07d2`](https://github.com/TimKleindick/general_manager/commit/08b07d2202cc705979135d4176b57afd6e7b0c22))

- Improve handling of many-to-many attributes in _sortKwargs method
  ([`ef94175`](https://github.com/TimKleindick/general_manager/commit/ef94175d8017abfd7a72550716445d8d65403717))

- Update __checkForInvalidKwargs to handle '_id_list' suffix in keys
  ([`db81620`](https://github.com/TimKleindick/general_manager/commit/db81620cde0d6b1252de322c7fa10d09956254a1))

### Refactoring

- Streamline create and update methods by consolidating attribute setting logic
  ([`475ca57`](https://github.com/TimKleindick/general_manager/commit/475ca57694e5e9e8ed7d0f55d17829dd86b6878b))

### Testing

- Add DatabaseInterfaceTestCase with validation and history management
  ([`b41d432`](https://github.com/TimKleindick/general_manager/commit/b41d43200500682d0182246a87743f4cdef83715))

- Add update method call in test_create_update_and_deactivate to verify reader assignment
  ([`072d9e8`](https://github.com/TimKleindick/general_manager/commit/072d9e8eba2969e6d77ad8144438271004e8bd58))


## v0.6.1 (2025-06-15)

### Bug Fixes

- Improve __repr__ method in CalculationBucket for clearer output
  ([`ca9d604`](https://github.com/TimKleindick/general_manager/commit/ca9d604baa251ff52572d419da7a27521667633d))

- Refine filtering logic in CalculationBucket to enhance clarity and functionality
  ([`fa9f573`](https://github.com/TimKleindick/general_manager/commit/fa9f573e455cd9fbb9792fa8bdb5389aa804ed43))

- Update error handling in getFieldType and clean up comments in _preCreate
  ([`3083626`](https://github.com/TimKleindick/general_manager/commit/3083626e754d8da40164881e1e71b3b764fa51a0))

- Update exception type in getFieldType method to KeyError for non-existent fields
  ([`9bec05e`](https://github.com/TimKleindick/general_manager/commit/9bec05ef869d29e590462fff496595a9e9ddce93))

### Testing

- Add comprehensive tests for CalculationBucket functionality and behavior
  ([`f7ad84c`](https://github.com/TimKleindick/general_manager/commit/f7ad84c9348ae680ab20328d57d6dcced64787e8))

- Add unit tests for CalculationInterface methods and functionality
  ([`043e09c`](https://github.com/TimKleindick/general_manager/commit/043e09c60de2f43e11e5cda7f1f0e1d670143d0d))

- Correct equality check in DummyGeneralManager to ensure proper comparison
  ([`b1ec08b`](https://github.com/TimKleindick/general_manager/commit/b1ec08b99184e4b06fd54ac5c093e1585a6f5079))

- Correct formatting in __repr__ method of CalculationBucket for consistency
  ([`cb6bd94`](https://github.com/TimKleindick/general_manager/commit/cb6bd94dc29b19741c7a94149b91328892eb692c))

- Remove print statement from test_first_last_empty_and_nonempty for cleaner output
  ([`3f421ce`](https://github.com/TimKleindick/general_manager/commit/3f421ce8fbdc264c501f39b65368a90c7213261d))

- Rename test file to databaseBasedInterface
  ([`3e61fb1`](https://github.com/TimKleindick/general_manager/commit/3e61fb1e835e75c7f586ecc4fc62e6fa823d524c))

- Update variable name in loops for consistency and clarity
  ([`1bcf82b`](https://github.com/TimKleindick/general_manager/commit/1bcf82bfddb25ecfee46ab5ccbad2b86fc4c45e8))


## v0.6.0 (2025-06-15)

### Bug Fixes

- __eq__ for groupBucket
  ([`0c33798`](https://github.com/TimKleindick/general_manager/commit/0c33798031815dccb3ae373501cf1d0bf7adcd37))

- Add __setstate__ method to restore current combinations in CalculationBucket
  ([`c2fa8a5`](https://github.com/TimKleindick/general_manager/commit/c2fa8a5064b4bbec4cf3643684f5e80f655e0928))

- Correct error message and type hint in groupBy and sort methods
  ([`bc19f79`](https://github.com/TimKleindick/general_manager/commit/bc19f79fa93d589368daba6d8d603ed2f39e94ee))

- Correct string formatting in CalculationBucket class
  ([`4c4b969`](https://github.com/TimKleindick/general_manager/commit/4c4b96986be0c21095f6c24296da36c6d27d3715))

- Enhance CalculationBucket initialization with filters, excludes, sort_key, and reverse parameters
  ([`98bf9d2`](https://github.com/TimKleindick/general_manager/commit/98bf9d22a83f90e6eefa39d92efeae5291c4d061))

- Optimize equality check in GroupManager by using hash comparison
  ([`41df94b`](https://github.com/TimKleindick/general_manager/commit/41df94bbe5cc2f0832c774ca6c70bcb351fe86e8))

- Optimize field value checks in DBBasedInterface by removing redundant calls to keys()
  ([`5447007`](https://github.com/TimKleindick/general_manager/commit/5447007d8512c35e4aa5174c545ccd182bc64720))

- Optimize group value handling in GroupBucket and remove unnecessary JSON serialization
  ([`e00acdc`](https://github.com/TimKleindick/general_manager/commit/e00acdc2339fac574f21d21edf5dd3c6bcf7db6d))

- Optimize length calculation in CalculationBucket by using generate_combinations directly
  ([`5976e0a`](https://github.com/TimKleindick/general_manager/commit/5976e0a00510dce77548c051d671611a8f236e2a))

- Optimize membership check in CalculationBucket.__contains__ method
  ([`a2afb2e`](https://github.com/TimKleindick/general_manager/commit/a2afb2e2a398ee45478972c424b6120603108255))

- Simplify and debug related model handling in DBBasedInterface
  ([`1f05cfd`](https://github.com/TimKleindick/general_manager/commit/1f05cfd41e6300f91676db658b0b4ebb930c02e7))

- Simplify equality check in GroupManager by removing redundant instance check
  ([`ed3219c`](https://github.com/TimKleindick/general_manager/commit/ed3219cc7188cd46fe09696bd35b7b418ecc24c3))

- Simplify state retrieval in __setstate__ and iterate over input_fields directly
  ([`8e56b29`](https://github.com/TimKleindick/general_manager/commit/8e56b2938640d10a828fbb7302490c3cfcb36ae1))

- Slicing in calculationBucket
  ([`c68739a`](https://github.com/TimKleindick/general_manager/commit/c68739a14e3d45f60b97fce4f60740e1400b00dd))

- Sort group_by_values using string representation for consistent ordering
  ([`f13022e`](https://github.com/TimKleindick/general_manager/commit/f13022e0af733c755bf82791bed0801b91fd7508))

- Update identification access in DatabaseBucket methods
  ([`f3bc0cd`](https://github.com/TimKleindick/general_manager/commit/f3bc0cd64b2ad3428eb471565a435c72da0ae2d6))

- Update user type check to use AbstractUser in getUserWithId method
  ([`3e259e5`](https://github.com/TimKleindick/general_manager/commit/3e259e5f9fe3aa25fb1c6aeb10c3f2f9a2666151))

### Chores

- Update requirements to use base.txt for consistency
  ([`3584581`](https://github.com/TimKleindick/general_manager/commit/35845817c264892b77beab57f6a1585a0a7f58d6))

### Documentation

- Shorten project description for clarity and conciseness
  ([`3b87ff7`](https://github.com/TimKleindick/general_manager/commit/3b87ff7e8b8a9c76eef76eaf2905a76426d31ac4))

- Split requirements files to development and production environments
  ([`7f3ef5f`](https://github.com/TimKleindick/general_manager/commit/7f3ef5f933f86d96dfcb4ff569293b910085a355))

### Features

- Implement __hash__ method in GroupManager for improved object hashing
  ([`99ffb6e`](https://github.com/TimKleindick/general_manager/commit/99ffb6edfe6448d9840cb1eb157144dbec887565))

### Refactoring

- Clean up imports and simplify PermissionDataManager usage in BasePermission
  ([`d6bb292`](https://github.com/TimKleindick/general_manager/commit/d6bb292ac386a0214751d15f2a0d66741a3d57b5))

- Lambda to named function for combination generation
  ([`73bb1a0`](https://github.com/TimKleindick/general_manager/commit/73bb1a01f7545ddb91a749f5e204d1f57e29e8b2))

- Move calculationBucket to own file
  ([`6e4d441`](https://github.com/TimKleindick/general_manager/commit/6e4d441117b7d019e567849e4840195c76a087da))

- Remove TYPE_CHECKING import and streamline GeneralManager import
  ([`c3434f5`](https://github.com/TimKleindick/general_manager/commit/c3434f576bb970aaa1d808bea5ed3a7eb80ea859))

- Remove unnecessary blank lines and improve code readability in ReadOnlyInterface
  ([`618e674`](https://github.com/TimKleindick/general_manager/commit/618e674aa93fe7db15113c52f6ea2b78435b1be3))

- Remove unnecessary blank lines and improve code readability in test_generalManager
  ([`ae982da`](https://github.com/TimKleindick/general_manager/commit/ae982da52c4e3798d18c721f31ac46730315bd29))

- Remove unnecessary blank lines and improve docstring clarity in DummyInterface and
  DatabaseBucketTestCase
  ([`9c40426`](https://github.com/TimKleindick/general_manager/commit/9c40426168fdf3ffaaed644cde46ebbb5036e419))

- Remove unnecessary blank lines and improve docstring formatting in DummyInterface and
  InterfaceBaseTests
  ([`f7e856a`](https://github.com/TimKleindick/general_manager/commit/f7e856a05e79ac14ba236f955c9ad33b4e83fd15))

- Remove unnecessary blank lines in DBBasedInterface and related methods
  ([`2e00b5c`](https://github.com/TimKleindick/general_manager/commit/2e00b5c443c1cc1196d672e5e88924c2da3bf95d))

- Rename TestInterface to DummyInterface for clarity in test cases
  ([`0789a51`](https://github.com/TimKleindick/general_manager/commit/0789a51007fbf5e4f76baa5a3220b8ff8448df88))

- Simplify field existence checks in DBBasedInterface
  ([`53b4098`](https://github.com/TimKleindick/general_manager/commit/53b40984f9275c46912eb7111c63f5ce039e9484))

- Simplify generator implementation in GroupBucket.__iter__ method
  ([`908be9f`](https://github.com/TimKleindick/general_manager/commit/908be9fc26e6f327db543b86c632ac89ea627292))

- Split interface and bucket
  ([`fe779bf`](https://github.com/TimKleindick/general_manager/commit/fe779bfe8237851a644d652839de9dddc7e88f1b))

- Update filter and exclude definitions to use None as default and improve queryset handling
  ([`fa229d3`](https://github.com/TimKleindick/general_manager/commit/fa229d328412bf5078147ca83b1a1f50acef0be6))

### Testing

- Add comprehensive tests for DatabaseBasedInterface
  ([`64fb815`](https://github.com/TimKleindick/general_manager/commit/64fb8150d2f1618781730bc7d5fcfc16769a1031))

- Add DatabaseBucket test case with UserManager integration
  ([`9ea7c22`](https://github.com/TimKleindick/general_manager/commit/9ea7c2203544beccaf7760f372b0d1d65f016a4f))

- Remove unnecessary blank lines and improve exception message clarity in GeneralManagerMetaTests
  ([`5594d79`](https://github.com/TimKleindick/general_manager/commit/5594d794def777d203a404d52ab28ca8c0b40937))

- Rename test_possible_values_invalid_type to test_invalid_kwargs for clarity
  ([`e4b6f45`](https://github.com/TimKleindick/general_manager/commit/e4b6f453667ce656724e5fabb93420ac59d002f5))

- Sorting database bucket
  ([`80bb51e`](https://github.com/TimKleindick/general_manager/commit/80bb51eb45ee84513225e931569430bb0c249ed4))


## v0.5.2 (2025-06-09)

### Bug Fixes

- Change exception type from TypeError to ValueError in GroupBucket class
  ([`26df806`](https://github.com/TimKleindick/general_manager/commit/26df806a241a124ae094f3ab8aeaf77ba7ca3268))

- More efficiency through arg in dict instead of arg in dict.keys()
  ([`d16200e`](https://github.com/TimKleindick/general_manager/commit/d16200e7d3e7bef3d0454208bbe2805589f04b0d))

### Documentation

- Add AGENTS.md
  ([`c2760f7`](https://github.com/TimKleindick/general_manager/commit/c2760f7ff382b9fb1151c9d20ca220cd0a6d5ae0))

- Add Input class documentation
  ([`707aea3`](https://github.com/TimKleindick/general_manager/commit/707aea37554c0559c7ad13bc88b7fb20b7c45d1d))

- Clarify usage of Input class in context of GeneralManager initialization
  ([`e900175`](https://github.com/TimKleindick/general_manager/commit/e9001759a9c729d3158f3a14a383ac8b5107021b))

- Remove unnecessary blank lines in DatabaseBucket class docstrings
  ([`67742a2`](https://github.com/TimKleindick/general_manager/commit/67742a29cd6709233f096a870f57207d5fc9270b))

- Translate and update README
  ([`695dcf7`](https://github.com/TimKleindick/general_manager/commit/695dcf7afc4299ca7a0d1623817173e383161780))

- Update AGENTS.md to use English for clarity and consistency
  ([`1f038e6`](https://github.com/TimKleindick/general_manager/commit/1f038e68e690070de16bf763f2133e5cadaf63c9))

- Update comments for clarity and consistency in InterfaceBase
  ([`86dbe7e`](https://github.com/TimKleindick/general_manager/commit/86dbe7e4076a1dbcff71175ef28054df7838ee62))

### Testing

- Add tests for InterfaceBase and Bucket implementations
  ([`7b7f47d`](https://github.com/TimKleindick/general_manager/commit/7b7f47d51170c3c39b751a5504f82a1695f9b7f2))

- Correct attribute access for _group_by_keys in BucketTests
  ([`97b5bf3`](https://github.com/TimKleindick/general_manager/commit/97b5bf33bd35f3770acd5fe048cfa5d32754d143))

- Missing """ led to problems
  ([`2e917b3`](https://github.com/TimKleindick/general_manager/commit/2e917b3cb1f10f4b750668a136ddfbb193678c85))


## v0.5.1 (2025-06-08)

### Bug Fixes

- Implement equality check for GroupBucket and update group_by method
  ([`14b0a0c`](https://github.com/TimKleindick/general_manager/commit/14b0a0c2fa1f6b9c7c8128e5cf7ead62d9d1b372))

- Optimize data aggregation logic in GroupManager for boolean types
  ([`105e60e`](https://github.com/TimKleindick/general_manager/commit/105e60ed1d4c7784deabe0a65ffab84bf46b6937))

- Remove unused __hash__ method from GroupManager
  ([`0e9335e`](https://github.com/TimKleindick/general_manager/commit/0e9335e65c65b1c10f2a4e1cfe508ef123a5c471))

- Simplify sorting logic in GroupBucket by removing unnecessary list comprehension
  ([`0417435`](https://github.com/TimKleindick/general_manager/commit/0417435f68047cf7bbb0cc26bec5272cc5cb6166))

- Sort group_by_values and improve sorting logic in GroupBucket
  ([`f0fe417`](https://github.com/TimKleindick/general_manager/commit/f0fe417ed83a9f3765116903765151b3e66102d9))

- Update data aggregation in GroupManager to avoid duplicates
  ([`016d254`](https://github.com/TimKleindick/general_manager/commit/016d254a9a7677eec6ae63a5aa0126fa69bbd1ef))

### Refactoring

- Rename GroupedManager to GroupManager and update references
  ([`f5e6e50`](https://github.com/TimKleindick/general_manager/commit/f5e6e50d49e03dc2d28e274c01e605ba6e552a44))

### Testing

- Add comprehensive tests for GroupBucket and GroupManager functionality
  ([`088be38`](https://github.com/TimKleindick/general_manager/commit/088be38023e8c39d2272484bd8926b56f40eecde))

- Clean up imports and improve GroupBucket test assertions
  ([`cec9f8d`](https://github.com/TimKleindick/general_manager/commit/cec9f8d0d45c8a250f3965f1465c4c7aa71e0850))

- Correct type definition for date in DummyInterface and add setup/teardown for tests
  ([`81199ca`](https://github.com/TimKleindick/general_manager/commit/81199ca04938cd7255e52eb83f15d0d8b3201f5e))


## v0.5.0 (2025-06-05)

### Documentation

- Add arithmetic examples for Measurement
  ([`16874c4`](https://github.com/TimKleindick/general_manager/commit/16874c4a284f9c4533f5b2a35fdd7df7d5fb439f))

### Features

- Improve error handling in propertie methods
  ([`3b007ed`](https://github.com/TimKleindick/general_manager/commit/3b007edeb83c60b8fadb57ebe11ce38c56487eec))

### Refactoring

- Remove unused import from test_generalManagerMeta.py
  ([`0a61bed`](https://github.com/TimKleindick/general_manager/commit/0a61bedd56a15f5fb1037cee08c641bebe8a5658))

### Testing

- Add comprehensive tests for GeneralManager properties
  ([`97d6677`](https://github.com/TimKleindick/general_manager/commit/97d66771be9159197a5277bc5e614c0345281a55))

- Add tests for GeneralManagerMeta __new__ method
  ([`3498186`](https://github.com/TimKleindick/general_manager/commit/34981869821611d9fba03d488fa5e3159f2c34f7))


## v0.4.6 (2025-06-04)

### Bug Fixes

- Pointer error in __parse_identification
  ([`d6b67c2`](https://github.com/TimKleindick/general_manager/commit/d6b67c2dc1b6f7b8df7542a587434fbea68e4b36))

### Refactoring

- Relocate AutoFacotory to seperate file
  ([`a970130`](https://github.com/TimKleindick/general_manager/commit/a970130a8674a4fe3ab28e35a9a139847aaa64ed))

- Replace getattr with direct access
  ([`054f1a9`](https://github.com/TimKleindick/general_manager/commit/054f1a9d50da5165a5ccc261dcc5789dcff69618))

### Testing

- Add AutoFactory test cases
  ([`a3fd909`](https://github.com/TimKleindick/general_manager/commit/a3fd909b35d39148277dfc4ff6ee20fb6db6df1e))

- Add unit test for GeneralManager deactivate class method
  ([`2e2a3b5`](https://github.com/TimKleindick/general_manager/commit/2e2a3b53dea752dd3248d85f2931fff855411870))

- Add unit tests for GeneralManager functionality
  ([`0b9235d`](https://github.com/TimKleindick/general_manager/commit/0b9235dfcd7de29aa0248c32f8c012835512aad3))

- Enhance AutoFactoryTestCase with teardown and type hints
  ([`958b2c3`](https://github.com/TimKleindick/general_manager/commit/958b2c338c8b2edc88d2991061e654a5f694a4cd))

- Update comments for clarity in GeneralManagerTestCase
  ([`8f6e0f0`](https://github.com/TimKleindick/general_manager/commit/8f6e0f0c18452f147cfec74662b8508da4e8ed99))


## v0.4.5 (2025-05-28)

### Bug Fixes

- Improve string parsing and comparison error handling in Measurement class
  ([`53f7543`](https://github.com/TimKleindick/general_manager/commit/53f7543f0bba0d9221f5df6d861dc34c473ba368))

### Testing

- Enhance Measurement class tests for addition, comparison, and pickling
  ([`c1acda2`](https://github.com/TimKleindick/general_manager/commit/c1acda27c1b36a4c1d98a7f2b55853e651990f52))


## v0.4.4 (2025-05-28)

### Bug Fixes

- Try to adjust changelog
  ([`3b60789`](https://github.com/TimKleindick/general_manager/commit/3b6078923e9ed3baf106bbf4062a1da772e551f0))

- Try to adjust changelog
  ([`2531dc1`](https://github.com/TimKleindick/general_manager/commit/2531dc1b774bffc14659591a44f3417da637f257))

- Try to adjust changelog
  ([`c990369`](https://github.com/TimKleindick/general_manager/commit/c990369579dea47d3812758bb77c56066dbc5381))

- Try to adjust changelog
  ([`cc92c5e`](https://github.com/TimKleindick/general_manager/commit/cc92c5e1f83b30c5d8959de6c61bdede980ae14a))

- Try to adjust changelog
  ([`7eab154`](https://github.com/TimKleindick/general_manager/commit/7eab154f0b9658ebe55311e59d287cab3770d595))

- Try to adjust changelog
  ([`6b0b601`](https://github.com/TimKleindick/general_manager/commit/6b0b6012ca164c1d73d71f73671ddb531bc25a4e))

### Continuous Integration

- Fixed pipeline
  ([`9831330`](https://github.com/TimKleindick/general_manager/commit/9831330bf090a04d9b8eb95aceda6e0fab29082e))


## v0.4.3 (2025-05-28)

### Bug Fixes

- Changelog
  ([`fdb1176`](https://github.com/TimKleindick/general_manager/commit/fdb117653a4269e1f6ba0d1e5072f82fe4dd3291))

- Semantic-releasec
  ([`eb80961`](https://github.com/TimKleindick/general_manager/commit/eb8096108ad35550dcacb427208d67fa5d97326f))

- Update the Command to also update the Changelog
  ([`d323a08`](https://github.com/TimKleindick/general_manager/commit/d323a081110c00eee99ab478348ad18407c67266))


## v0.4.2 (2025-05-28)

### Bug Fixes

- Improved Deploy Pipeline to work SSH based for commits
  ([`42a9dc9`](https://github.com/TimKleindick/general_manager/commit/42a9dc94e67207eaa3a6c6a009e7bc555b42a64b))

- Last chance for ssh commit
  ([`642f60c`](https://github.com/TimKleindick/general_manager/commit/642f60c49ce544bcefe7f60c554a93953b6cc4c1))

### Continuous Integration

- Add condition to trigger release job on push event
  ([`40afbe5`](https://github.com/TimKleindick/general_manager/commit/40afbe5e51866d9092ac02d496510c7bd5e7b5f2))

- Add ignore-token-for-push to use ssh
  ([`4773fb4`](https://github.com/TimKleindick/general_manager/commit/4773fb4cfc26b609d7d906b1b79fc818f5bd75f1))

- Add remote configuration for semantic release
  ([`73fe533`](https://github.com/TimKleindick/general_manager/commit/73fe533d5d4c616d7bbe7c7a6be7bca040a66917))

- Add step to configure SSH known_hosts for GitHub
  ([`31c5fe6`](https://github.com/TimKleindick/general_manager/commit/31c5fe6958c76c4ae8641db6c5b0d14dfdfabffa))

- Change pyproject.toml
  ([`7bd078e`](https://github.com/TimKleindick/general_manager/commit/7bd078ea960202a751071de98be9d4b28dd0c29a))

- Fix deploy key name
  ([`87479b5`](https://github.com/TimKleindick/general_manager/commit/87479b5e1f7c367e59f73b8f5338cf70285ecfe3))

- Ignore_token_for_push: true
  ([`eac1959`](https://github.com/TimKleindick/general_manager/commit/eac1959ccd9f8f506e4b8a9b8530ec433a77be47))

- Removed activation on tags for workflow
  ([`1e76c97`](https://github.com/TimKleindick/general_manager/commit/1e76c970e01e36304107d075a8b76a6a8f22e100))

- Removed url from settings
  ([`041aebd`](https://github.com/TimKleindick/general_manager/commit/041aebd1d2153db88bbfb87df4f2650e6a059146))

- Update Git remote URL to use SSH format
  ([`6d782a0`](https://github.com/TimKleindick/general_manager/commit/6d782a0355bce23402e6582a646f3d826f756214))

- Update SSH checkout configuration in workflow
  ([`4f887f6`](https://github.com/TimKleindick/general_manager/commit/4f887f6d968f3937ecf6d8bad18f6af688a2988e))

- Update SSH known_hosts setup and remove Git remote URL from pyproject.toml
  ([`3f8e74b`](https://github.com/TimKleindick/general_manager/commit/3f8e74ba45ba90695741bff2edd430f464fead12))

- Update SSH known_hosts setup for improved security
  ([`aedb7f9`](https://github.com/TimKleindick/general_manager/commit/aedb7f9b372072fc3dc0a3e88563600812f01b05))

- Workflow settings change
  ([`7305a97`](https://github.com/TimKleindick/general_manager/commit/7305a97351d673ddb99a4048b831f94eecfed1d2))

### Testing

- Fix m2m with factory can return empty list result
  ([`980f789`](https://github.com/TimKleindick/general_manager/commit/980f7895fe7b7b926b8521565615e92bb82b1894))


## v0.4.1 (2025-05-26)

### Bug Fixes

- Ci pipeline
  ([`07c258f`](https://github.com/TimKleindick/general_manager/commit/07c258fd817686ef145f2d21e93fed591404672f))

### Continuous Integration

- Add checkout
  ([`f7a5284`](https://github.com/TimKleindick/general_manager/commit/f7a5284aa99ec389274f94254196f0a5bb10636f))

- Add github to known hosts
  ([`cbe4d75`](https://github.com/TimKleindick/general_manager/commit/cbe4d755e84a04e778acd9b64f76787d89ed800e))

- Add remote to pyproject toml to enable ssh based releases
  ([`8dc2edb`](https://github.com/TimKleindick/general_manager/commit/8dc2edb92125770e7b96942eb7a5721bb7344ef8))

- Add ssh prefix for remote url
  ([`b9341b8`](https://github.com/TimKleindick/general_manager/commit/b9341b8ce2eb8b58387fff9999c2aeccfe55e238))

- Go back to basic
  ([`211827b`](https://github.com/TimKleindick/general_manager/commit/211827b88ebded3040562f8104217497ae895eef))

- Go back to https
  ([`db8365e`](https://github.com/TimKleindick/general_manager/commit/db8365e43835c7e9d611702e19fcca71caaba3df))

- Reorganize semantic release remote configuration in pyproject.toml
  ([`e51a097`](https://github.com/TimKleindick/general_manager/commit/e51a097ba7c0d4ca57fa1b8b6f1818d368184cad))

- Update remote configuration in pyproject.toml for semantic release
  ([`f9c2681`](https://github.com/TimKleindick/general_manager/commit/f9c26814d41ab4d2f753feab4dd4e0c219a423b9))


## v0.4.0 (2025-05-21)

- Initial Release
