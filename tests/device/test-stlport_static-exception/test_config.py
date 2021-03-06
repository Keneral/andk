def match_broken(abi, platform, device_platform, toolchain, subtest=None):
    # These were marked broken when we inherited them, so there's only one bug
    # for the whole group.
    legacy_broken = (
        'elide2',
        'new3',
        'terminate1',
        'weak1',
    )
    if subtest in legacy_broken:
        return toolchain, 'http://b/24541258'

    if subtest == 'badalloc1' and device_platform >= 23:
        return device_platform, 'http://b/26002885'

    if subtest == 'filter1' and device_platform >= 21 and toolchain == '4.9':
        return '{} {}'.format(device_platform, toolchain), 'http://b/24403847'

    if subtest == 'dyncast1' and toolchain == 'clang' and abi == 'x86_64':
        return '{} {}'.format(toolchain, abi), 'http://b/26085687'

    if (subtest == 'dyncast2_1' and toolchain == 'clang' and
        abi.startswith('x86')):
        return '{} {}'.format(toolchain, abi), 'http://b/26085687'

    return None, None
