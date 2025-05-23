# CHANGELOG


## v0.4.0 (2025-05-21)

### Bug Fixes

- Getmanytomanyfieldvalue
  ([`9ead241`](https://github.com/TimKleindick/general_manager/commit/9ead241c58b9c21941231d2b2245a494b789a6ae))

### Features

- Add magnitude and unit properties to Measurement class
  ([`6d09ac3`](https://github.com/TimKleindick/general_manager/commit/6d09ac39b6623013e59f219577fffe5d76ff7355))

- Add new lazy loading functions and corresponding tests for date, time, integer, decimal, boolean,
  and faker attributes
  ([`3e5ca27`](https://github.com/TimKleindick/general_manager/commit/3e5ca2714b18db47f2e11022b87bc53e6a9803a1))

### Refactoring

- Improve datetime handling and random instance creation in factories
  ([`e87d9f2`](https://github.com/TimKleindick/general_manager/commit/e87d9f240f7f0330b447535e606f75c26508a244))

- Remove type ignore comments from _generate, _create, and _build methods
  ([`cd9560c`](https://github.com/TimKleindick/general_manager/commit/cd9560c47fd74788324bbb2bd4516b00389a82db))

- Update import path for factory methods and add factoryMethods module
  ([`0517eaf`](https://github.com/TimKleindick/general_manager/commit/0517eafd7385e2ccb20dd68171a314a29b831322))

- Update test cases to improve clarity and consistency
  ([`2096ca3`](https://github.com/TimKleindick/general_manager/commit/2096ca32aa3bdfb4303509b6fc3ebd2a380fe690))

### Testing

- Add type ignore comments for evaluate method in TestGetFieldValue and TestRelationFieldValue
  ([`0017f45`](https://github.com/TimKleindick/general_manager/commit/0017f4507311c2e987ec525cfca3dea92fdaae6b))

- Add unit tests for LazyMeasurement, LazyDeltaDate, and LazyProjectName
  ([`12ee785`](https://github.com/TimKleindick/general_manager/commit/12ee78560db142908888c5a7624697fee97baff8))

- Enhance test factories with ManyToManyField support and refactor field value retrieval
  ([`c317803`](https://github.com/TimKleindick/general_manager/commit/c31780356191ede6d5229dfd48c76c2650cbcad5))

- Ensure dummy instance is included in ManyToManyField results only if not empty
  ([`25a9174`](https://github.com/TimKleindick/general_manager/commit/25a9174ca96b281e8b4534e0bad71b66b135dbde))

- Fix test_m2m_without_factory to use correct dummy instance
  ([`dbf9a3c`](https://github.com/TimKleindick/general_manager/commit/dbf9a3cdc6b4bb94bd5479678b79fcfb492ebac4))

- Implement comprehensive tests for get_field_value function across various field types
  ([`994f55e`](https://github.com/TimKleindick/general_manager/commit/994f55ead31ad36b09ef2383ad06beeaed0c1e24))

- Refactor tests to improve readability and consistency in exception handling
  ([`f0e06cb`](https://github.com/TimKleindick/general_manager/commit/f0e06cb66b07fb89c13d8d5cd22245265a6dc999))


## v0.3.2 (2025-05-18)

### Bug Fixes

- Capture_old_values & update docstrings to English and improve clarity
  ([`4d0dbf5`](https://github.com/TimKleindick/general_manager/commit/4d0dbf5be1692e31f694056aea5553f01b61d2df))

- Ensure string handling in generic_cache_invalidation and update test for old value scenarios
  ([`2d1071d`](https://github.com/TimKleindick/general_manager/commit/2d1071df7b1075b93d68bbb96057d16ff4cbf0cb))

- Improve generic_cache_invalidation logic for string operations
  ([`250a0e7`](https://github.com/TimKleindick/general_manager/commit/250a0e7d2f898f705b4462975587c79ca4e51662))

- Old value handling with operator
  ([`cd1ac5e`](https://github.com/TimKleindick/general_manager/commit/cd1ac5ea8b819b95f6f9a8b4b4be73629de53fd9))

- Update error message for lock acquisition and improve undefined value handling
  ([`de690aa`](https://github.com/TimKleindick/general_manager/commit/de690aa40b87c5101fe64549b6ea6a66614b0570))

### Continuous Integration

- Add webfactory/ssh-agent@v0.5.4
  ([`e70974e`](https://github.com/TimKleindick/general_manager/commit/e70974e3d84269efb910d0623419215f33669cb1))

- Add permissions for contents in test job
  ([`55260e0`](https://github.com/TimKleindick/general_manager/commit/55260e07f8f2a58c41c759ce3cf10875f86e0f0d))

- Add SSH key for repository checkout in GitHub Actions workflow
  ([`a3b06f9`](https://github.com/TimKleindick/general_manager/commit/a3b06f924a2ec6183febd05f989d51b9b8d3f1d9))

- Remove whitespaces
  ([`1a44152`](https://github.com/TimKleindick/general_manager/commit/1a4415203f48001ebb0874dc9fd5aed29bd27a88))

### Testing

- Add comprehensive tests for cache management functions
  ([`d89914f`](https://github.com/TimKleindick/general_manager/commit/d89914f0ff157e1cdb6f095e601b716859600a26))

- Add signal handling tests for dataChange decorator
  ([`459eabe`](https://github.com/TimKleindick/general_manager/commit/459eabedea97b3fc9f190dbd62eb8ef084a6b6ab))

- Add unit tests for acquire and release lock functionality
  ([`b7c70de`](https://github.com/TimKleindick/general_manager/commit/b7c70de4afec2cfa146acc7464f083443cda2848))

- Rename test for clarity in GenericCacheInvalidationTests
  ([`ce15f6d`](https://github.com/TimKleindick/general_manager/commit/ce15f6de3d2be783e0665cbdce761c339f1c25ea))


## v0.3.1 (2025-05-17)

### Bug Fixes

- Cache setting logic for nested cached functions
  ([`c94db78`](https://github.com/TimKleindick/general_manager/commit/c94db7893a0670b228fc6a44cbbc79a3730741de))

- Distinguish between cache miss and None result
  ([`ee3df6f`](https://github.com/TimKleindick/general_manager/commit/ee3df6fa8efd0734d6af600352465180de0d31af))

- Ensure proper cleanup of depth variable in DependencyTracker
  ([`8bd7432`](https://github.com/TimKleindick/general_manager/commit/8bd743222dfe2799631f28c92bbf1ae3dadda1b1))

- Improve cache handling imitation by adding pickle serialization in FakeCacheBackend
  ([`3e4d14b`](https://github.com/TimKleindick/general_manager/commit/3e4d14b74657780b1f70a9d4188ad0a58c556bb3))

- Improve docstrings for cache backend methods and test cases
  ([`74759a3`](https://github.com/TimKleindick/general_manager/commit/74759a37e627c61b92a74cd8f889106962e0387d))

- Reset thread-local storage in tests and adjust cache timeout for better isolation
  ([`5a059ab`](https://github.com/TimKleindick/general_manager/commit/5a059ab5ff7db933d702a93f8849057baeb0cc4c))

- Store dependecies of inner functions even with cache hit of inner function
  ([`f5171b4`](https://github.com/TimKleindick/general_manager/commit/f5171b44140b433261ac3b67c103535cf38db155))

- Update cache key generation to use qualified name instead of function name
  ([`32c2cdf`](https://github.com/TimKleindick/general_manager/commit/32c2cdf6c528153f69b92c12bd3d95e431779a6a))

### Refactoring

- Change test case class from django SimpleTestCase to unittest TestCase
  ([`04d3939`](https://github.com/TimKleindick/general_manager/commit/04d39399771b32da06a6e0ae964e6b26ad45c9d0))

- Move PathMap and PathTracer classes from cache to auxiliary
  ([`11201aa`](https://github.com/TimKleindick/general_manager/commit/11201aa01dfee75259bbf5cc87c8e22c11b73890))

- Remove unnecessary TYPE_CHECKING imports in pathMapping.py
  ([`ad6afad`](https://github.com/TimKleindick/general_manager/commit/ad6afad1c51ce4f473d6040d317daccbfc4a70f8))

- Remove unused import of defaultdict in cacheTracker.py
  ([`4885b59`](https://github.com/TimKleindick/general_manager/commit/4885b599305e8ac68d8d4ed2cb630e01e1a378db))

### Testing

- Add comprehensive tests for cache decorator functionality
  ([`ab0b509`](https://github.com/TimKleindick/general_manager/commit/ab0b509d871156099ebcd08ca1f56277cf5e7c67))

- Add comprehensive unit tests for make_cache_key function
  ([`20b9667`](https://github.com/TimKleindick/general_manager/commit/20b9667dc9be8d2865dfa755883bf938ae5c5570))

- Add test for make_cache_key with kwargs as args
  ([`2397c3b`](https://github.com/TimKleindick/general_manager/commit/2397c3b617b118178de1bff8acd89c18ed232a97))

- Add unit test for nested cache decorator with inner cache hit
  ([`d67f7f8`](https://github.com/TimKleindick/general_manager/commit/d67f7f81ccccac95048aa064ff917fb0d2d840d8))

- Add unit tests for DependencyTracker functionality
  ([`8aeadc7`](https://github.com/TimKleindick/general_manager/commit/8aeadc767dd815d062f99444d9dc73f43e881bbe))

- Add unit tests for ModelDependencyCollector functionality
  ([`bdcde99`](https://github.com/TimKleindick/general_manager/commit/bdcde99217a417e925f10d43258d4dc4e34fcf93))

- Change TestCase to SimpleTestCase for DependencyTracker tests
  ([`566068e`](https://github.com/TimKleindick/general_manager/commit/566068e03df8526e2ecbdd6e2914bb0b204084c3))

- Simplify exception handling in make_cache_key tests using combined context manager
  ([`7b93125`](https://github.com/TimKleindick/general_manager/commit/7b931254da0d66437a27d98ba4d9fca733936f71))

- Update exception type in dependency tracker test
  ([`41a370d`](https://github.com/TimKleindick/general_manager/commit/41a370d7f4729d61a535caed7bee77756992f973))


## v0.3.0 (2025-05-17)

### Features

- Implement CustomJSONEncoder for serializing datetime and GeneralManager objects
  ([`ec98a91`](https://github.com/TimKleindick/general_manager/commit/ec98a91a758f39e17cede8b8772be4150c00456a))

- Implement make_cache_key function for generating cache keys from function arguments
  ([`135365d`](https://github.com/TimKleindick/general_manager/commit/135365d81922380ab4b9e24d3cf9ad1231082dcd))

### Refactoring

- Cachedecorator for better maintainability
  ([`40b6ff6`](https://github.com/TimKleindick/general_manager/commit/40b6ff6ad9072256e8cd8ec3e7d9308939596553))

- Remove commented steps in cached decorator for cleaner code
  ([`d994a6b`](https://github.com/TimKleindick/general_manager/commit/d994a6b9a76ebe2fea36cdad108a5a527a017d70))

- Remove duplicate imports and improve DependencyTracker cleanup
  ([`c7450d1`](https://github.com/TimKleindick/general_manager/commit/c7450d1939aa35a9077fb67f0f7c9e060090ec10))

- Remove unnecessary import of general_manager_name in cacheTracker.py
  ([`dd57675`](https://github.com/TimKleindick/general_manager/commit/dd5767520ac9d6af65171cc67e03db2b5cfb9899))

- Remove unused imports and obsolete test
  ([`757e9da`](https://github.com/TimKleindick/general_manager/commit/757e9dab6c7c4a6ad491c8c67d176a31cd957256))

- Remove unused imports and update docstrings for clarity
  ([`103318f`](https://github.com/TimKleindick/general_manager/commit/103318f815a45827b0db026d75ac2a1c0919b774))

- Rename trackMe method to track in DependencyTracker for consistency
  ([`62f2cc1`](https://github.com/TimKleindick/general_manager/commit/62f2cc17754f3389322f186aaca3789e6070f9e4))

- Simplify setup for CustomJSONEncoderTests by removing unnecessary module patching
  ([`b3d529a`](https://github.com/TimKleindick/general_manager/commit/b3d529a5a9c9579d4d2e065746ffdf1c62588eec))

### Testing

- Jsonencoder
  ([`3fee1d2`](https://github.com/TimKleindick/general_manager/commit/3fee1d29e91376a5b7d873d73f0e3776166a6a92))


## v0.2.0 (2025-05-14)

### Bug Fixes

- Improve error handling for function handlers in rule system
  ([`c94d17a`](https://github.com/TimKleindick/general_manager/commit/c94d17a11a9c2332bf460ff29fafe08ad00737c1))

- Update error messages for sum, max, and min functions to include parentheses
  ([`29e44fa`](https://github.com/TimKleindick/general_manager/commit/29e44fae8a26e6f538cfe95dccbd631d5ecbd3e0))

### Continuous Integration

- Release only when version change is detected
  ([`e929f8e`](https://github.com/TimKleindick/general_manager/commit/e929f8e5d95bcdf742b281cf082cbdb2cd294971))

### Features

- Implement sum, max, and min handlers in rule system
  ([`1bfc1e6`](https://github.com/TimKleindick/general_manager/commit/1bfc1e6e60bb90d7a246e9652db72f5101dad2f1))

### Refactoring

- Clean up filterParser.py
  ([`8e077c6`](https://github.com/TimKleindick/general_manager/commit/8e077c6359d473547ae5813a18553f099a303e87))

- Handler for DRY and maintainability
  ([`a360ec6`](https://github.com/TimKleindick/general_manager/commit/a360ec69f44c052ca698bd15b9ce359bd68982d1))

- Remove getThreshold method and inline threshold calculations for clarity
  ([`93d0b40`](https://github.com/TimKleindick/general_manager/commit/93d0b40db1837de77ef3ae05de5e4906ae2084f6))

### Testing

- Add comprehensive tests for LenHandler, SumHandler, MaxHandler, and MinHandler
  ([`875c606`](https://github.com/TimKleindick/general_manager/commit/875c60679c5381302f9e3614d96aedf0a425860a))

- Add edge cases for gte/lte/exact
  ([`fe11010`](https://github.com/TimKleindick/general_manager/commit/fe1101044cb036a0bc13052570c740413d24649b))

- Filterparser for full coverage
  ([`605f8a8`](https://github.com/TimKleindick/general_manager/commit/605f8a846dcc9ca65a2d448b6bca0dd944bc5427))

- Improve error messages for sum, max, and min handlers for clarity and consistency + add edge cases
  ([`078a806`](https://github.com/TimKleindick/general_manager/commit/078a806d7830268bc928b119a375f1248c3bbc31))

- Other numeric types for noneToZero
  ([`ff3c310`](https://github.com/TimKleindick/general_manager/commit/ff3c3106b2265ef3ea8c1a49458e9378662cd02f))


## v0.1.2 (2025-05-13)

### Bug Fixes

- Typehint for filter/exclude in databaseInterface
  ([`e70e550`](https://github.com/TimKleindick/general_manager/commit/e70e55041778264f0f8704828d281efa822faa26))

### Testing

- 100% coverage for input
  ([`8f57f8a`](https://github.com/TimKleindick/general_manager/commit/8f57f8add6a24a53a425618f0c0f4540d27027c8))

- Nonetozero for full coverage
  ([`4992a73`](https://github.com/TimKleindick/general_manager/commit/4992a736331f2a83c7a7e8e2fffa0e89f9349336))

- Pytest config in vscode
  ([`3a69c57`](https://github.com/TimKleindick/general_manager/commit/3a69c57f2cd99e7988158cbaa3a5142135103d12))


## v0.1.1 (2025-05-11)

### Bug Fixes

- Remove required, editable, defaultValue from MeasurementType
  ([`733a1ae`](https://github.com/TimKleindick/general_manager/commit/733a1ae9804797d88871c8bb0f101343878eb195))

### Testing

- Fix test for removed required, editable, defaultValue
  ([`34be32a`](https://github.com/TimKleindick/general_manager/commit/34be32aab05748dd46eb131fecf3264b0b5e9eab))


## v0.1.0 (2025-05-11)

### Continuous Integration

- Add build and twine to action
  ([`37dd646`](https://github.com/TimKleindick/general_manager/commit/37dd6461e8112d58f1421f552370719ce9d89d69))

- Change build command location into pyproject
  ([`41115a7`](https://github.com/TimKleindick/general_manager/commit/41115a760f894bafbe7a216d91bacfbf13661c20))

- Manal build process
  ([`d2db282`](https://github.com/TimKleindick/general_manager/commit/d2db2829d19ddd0af6b01be75310a8b5abf0d415))

- Update github action workflow for automatic version sync
  ([`b1f104c`](https://github.com/TimKleindick/general_manager/commit/b1f104cbca8860247c363d567a9c9f47cac45711))

- Update to github action, added automatic versioning
  ([`bd60b52`](https://github.com/TimKleindick/general_manager/commit/bd60b528849e7f88f6ca025476e676964d24e117))

### Testing

- Add some graphql tests
  ([`bf06d84`](https://github.com/TimKleindick/general_manager/commit/bf06d8459b7819583345120b8c664507289ccec6))


## v0.0.0 (2025-05-06)

### Bug Fixes

- Automatic tests with pytest
  ([`6b89e81`](https://github.com/TimKleindick/general_manager/commit/6b89e81faeba4f32c5fdcb4b877024d3af657000))

- Blank and null for measurementField
  ([`f28f115`](https://github.com/TimKleindick/general_manager/commit/f28f11522319f5ae0f3fd0b2bfea2433b9e3a921))

- Circular import
  ([`c028554`](https://github.com/TimKleindick/general_manager/commit/c028554c82cfa9678dcd5205b1a902bef22c30ee))

- Combination of filter permission and not filter permission
  ([`51af5db`](https://github.com/TimKleindick/general_manager/commit/51af5dbde32f8ab005d101605d8e0599a4cb0125))

- if one permission defines a filter and one does not - This leads to NO filter --> every entry is
  findable

- Field permissions
  ([`5ce3966`](https://github.com/TimKleindick/general_manager/commit/5ce39666d35e50bda4909acc11c0751aa943e38e))

- Field type
  ([`65d747d`](https://github.com/TimKleindick/general_manager/commit/65d747dd7ce613657bc4ea5c163184d1c2928045))

- Filter condition with permissions
  ([`88b342c`](https://github.com/TimKleindick/general_manager/commit/88b342caa83b2ed099885394f7587d806d935559))

- no defined permission led to all objects instead of no filter

- Foreignkey relation with general manager
  ([`6e2667f`](https://github.com/TimKleindick/general_manager/commit/6e2667fbb99d3035be783bb09592691606fb92bb))

- Id to identification to match new standard
  ([`3905f82`](https://github.com/TimKleindick/general_manager/commit/3905f82b436bb7c296765a72ee41b02d42ccd8ae))

- Identification for comparision
  ([`7e31922`](https://github.com/TimKleindick/general_manager/commit/7e31922849a0a1f8f5a1618b232bc5b6fd916c02))

- Info object in graph ql tests
  ([`31a290a`](https://github.com/TimKleindick/general_manager/commit/31a290add992c9aaf3b77c20ea0462bed58aa559))

- Multiple permissions for permission filter
  ([`48104dd`](https://github.com/TimKleindick/general_manager/commit/48104dd8e70ae77a76e0205529717be955c73d22))

- No more default values for page and page_size
  ([`e05afba`](https://github.com/TimKleindick/general_manager/commit/e05afbaa123b68a66578383453dbe8361bb15fc7))

- Permissions in sub queries
  ([`3a7aac7`](https://github.com/TimKleindick/general_manager/commit/3a7aac7339efe254c0bc8976eece9ee98a792a87))

- Prototype update to use new possibilities
  ([`4171f1b`](https://github.com/TimKleindick/general_manager/commit/4171f1b5c7e0fed3a1d20797a7d4bba7476ee1c7))

- Remove contact information
  ([`cd41d15`](https://github.com/TimKleindick/general_manager/commit/cd41d15192f896bb91742c27465f89893f2bef82))

- Rule with type hints
  ([`907352b`](https://github.com/TimKleindick/general_manager/commit/907352b05235996e75ac0425999893f488cb65f5))

- Test runner
  ([`2d7db29`](https://github.com/TimKleindick/general_manager/commit/2d7db2908c067c2d02538685cf7672edffebefe1))

- Type annotations
  ([`38b54df`](https://github.com/TimKleindick/general_manager/commit/38b54df3bc70f45b9ec4310f1163a175261bec72))

- Type annotations
  ([`02698a2`](https://github.com/TimKleindick/general_manager/commit/02698a25ef51e6b5d3eba0b22899d2086fbbb0a6))

- Type hint adjusts
  ([`8a7b690`](https://github.com/TimKleindick/general_manager/commit/8a7b6907fd7cf672a011736a93ec3ee99a40c2ef))

- Type hints
  ([`aaf7dd7`](https://github.com/TimKleindick/general_manager/commit/aaf7dd7e56e9f2f635148600a89d9ffc1a59d862))

### Features

- __or__ operation for GeneralManager
  ([`8a74100`](https://github.com/TimKleindick/general_manager/commit/8a74100583d38e5ea3fb9f191b9f64a7ffe9d2fb))

- __repr__ for calculation bucket
  ([`5271990`](https://github.com/TimKleindick/general_manager/commit/5271990737b082d4ea0acd8279055c36259fb11b))

- Add editable to measurementField
  ([`a1b5ffa`](https://github.com/TimKleindick/general_manager/commit/a1b5ffa6a52d2d28995718e7479a42903cb96f42))

- Add is_required, is_editable and default to getAttributeType
  ([`fbecfec`](https://github.com/TimKleindick/general_manager/commit/fbecfec1346292a3edd391ca43910c4405d32bd4))

- first step towards automatic mutation creation

- Add requirements.txt
  ([`e560323`](https://github.com/TimKleindick/general_manager/commit/e560323e425267461f52fd4ba9482840dc3868f9))

- Add support for not GeneralManager Foreignkeys
  ([`0783cbc`](https://github.com/TimKleindick/general_manager/commit/0783cbcb6137f97f4bb702577938eb7daeb3c28b))

- Add tests for managerBasedPermission
  ([`f95b8cf`](https://github.com/TimKleindick/general_manager/commit/f95b8cf25e74d257359e22da874cad58553b0e55))

- Auto redirect to /graphql url
  ([`ec180a8`](https://github.com/TimKleindick/general_manager/commit/ec180a81ad4687fc9f6bbdcbb3557abadcef0229))

- Base permission tests
  ([`5951ca2`](https://github.com/TimKleindick/general_manager/commit/5951ca210745a7a41906a5b62b5bd3fa8fe97baa))

- Create auto mutations for every generalManagerClass
  ([`375cfd9`](https://github.com/TimKleindick/general_manager/commit/375cfd9b5a62affa3b24c3f349e5ac16190a514b))

- Default graphql mutations for manager class project
  ([`d18c456`](https://github.com/TimKleindick/general_manager/commit/d18c456e3cf7b362403b4513839488eacfab0e83))

- Dependency based cache invalidation
  ([`e4aec34`](https://github.com/TimKleindick/general_manager/commit/e4aec34dce69e8f65213304cd1cca87581f0d579))

- Enable __based_on__ permissions
  ([`228a740`](https://github.com/TimKleindick/general_manager/commit/228a740e1bcc640d6cbcd6add24f7290394680ba))

- Enable Object Input Types for schema
  ([`d9527f8`](https://github.com/TimKleindick/general_manager/commit/d9527f8e9f6e11b2accae2ae0d89a7c9f4c87e81))

- filter and exclude method get better hints in schema

- Enable pagignation
  ([`cc719ad`](https://github.com/TimKleindick/general_manager/commit/cc719adbcf226c48e03f73659488a22c180d74bd))

- Enable pickling of measurement objects
  ([`ae67d30`](https://github.com/TimKleindick/general_manager/commit/ae67d30a64e8c9ded4c1b091f06ab5db042a25f5))

- Graphqlmutation decorator to create custom mutations
  ([`16c7042`](https://github.com/TimKleindick/general_manager/commit/16c7042730477c0e84259d039997fa7f3a22d7bc))

- Implement __or__ on calculationInterface
  ([`a412b55`](https://github.com/TimKleindick/general_manager/commit/a412b55c20279eec3df6144231cf68fbd7ba7626))

- Implement caching decorator and auto use for graphQlProperties
  ([`7005991`](https://github.com/TimKleindick/general_manager/commit/7005991d29063d0f2bc13fdd492daf54a170db77))

- Implement group_by for buckets
  ([`746d554`](https://github.com/TimKleindick/general_manager/commit/746d5541aa487b481339930817663eab54f39ec9))

- Implement path tracing for generalManager
  ([`b39dd0c`](https://github.com/TimKleindick/general_manager/commit/b39dd0c9da82a941370d93784448a7c2a001ab19))

- Implement sort by
  ([`b8b36f0`](https://github.com/TimKleindick/general_manager/commit/b8b36f0c8908e03fcf30108d8c1cd1b5732d13fe))

- Is now installable
  ([`db32177`](https://github.com/TimKleindick/general_manager/commit/db32177e0c438b98fad26f18f71a60968454b6de))

- Permission checks for update/create/deactivate
  ([`35ccc48`](https://github.com/TimKleindick/general_manager/commit/35ccc48ec342b809dc58617b7a8547bd71df29f6))

- Read permissions for graphql interface
  ([`c48d6a2`](https://github.com/TimKleindick/general_manager/commit/c48d6a27486c645f3c85313a9995a65b047e4a98))

- permission_functions with single data check and overall filter method to increase performance -
  define syntax for manager based permissions - add permission data manager to handle change
  requests

- Set cache backend settings
  ([`f6364d0`](https://github.com/TimKleindick/general_manager/commit/f6364d0566015d553f58dc33bdc20180193ef54e))

- Update to python 3.13
  ([`3f351b8`](https://github.com/TimKleindick/general_manager/commit/3f351b87681cd9b5841605fac7a838a859c69019))

### Refactoring

- Graphql api
  ([`a28b109`](https://github.com/TimKleindick/general_manager/commit/a28b109add342e1ae25fba217526e4d8565d7d26))

- Move parse filter to auxiliary methods
  ([`87e66a6`](https://github.com/TimKleindick/general_manager/commit/87e66a68776913acfc432e7dc94c61667fbe81a3))

- Strukture to match PEP 420 / PEP 517
  ([`dbbf170`](https://github.com/TimKleindick/general_manager/commit/dbbf17037b2e472877202e8123b74541fbd5f484))
