import click

from . import crypto_svc, retrieval_svc, status_svc


@click.command(no_args_is_help=True)
@click.option('--hash_id',
              help='The hash of a recording from Verum.')
@click.option('--url',
              help='A url of a Verum file.')
@click.option('--id',
              help='ID if a recording from Verum.')
@click.option('--zipfile',
              help='local path to a zip file from a Verum recording.')
@click.option('--host', default="https://verumjourno.com",
              help="The verum server. Defaults to https://verumjourno.com")
@click.option('-v', '--verbose', count=True,
              help="More information out")
@click.option('-p', '--preserve', is_flag=True,
              help="Preserve downloaded artifacts")
def main(hash_id, url, id, zipfile, host, verbose, preserve):
    """Verify the cryptographic authenticity of a Verum recording."""
    if not any((hash_id, url, id, zipfile)):
        return

    if hash_id:
        status_svc.start(f"\nVerify Authenticity of Hash: {hash_id}\n",
                         nl=True)
        status_svc.start("Locating and retrieving files")
        fetched = retrieval_svc.get_by_hash_id(hash_id, host)
    elif id:
        status_svc.start(f"\nVerify Authenticity of Recording ID: {id}\n",
                         nl=True)
        status_svc.start("Locating and retrieving files")
        fetched = retrieval_svc.get_by_uuid(id, host)
    elif url:
        status_svc.start(f"\nVerify Authenticity of Url: {url}\n",
                         nl=True)
        status_svc.start("Locating and retrieving files")
        fetched = retrieval_svc.get_by_url(url)
    else:
        status_svc.start(f"\nVerify Authenticity of Zip File: {zipfile}\n",
                         nl=True)
        status_svc.start("Locating and retrieving files")
        fetched = retrieval_svc.get_by_zip(zipfile)
    status_svc.prog()
    if not fetched:
        status_svc.fail()
        return
    status_svc.success()

    status_svc.start("Loading public key files")
    device_key = retrieval_svc.load_key("device.pem")
    verum_key = retrieval_svc.load_key("verum.pem")
    status_svc.prog()
    if device_key and verum_key:
        status_svc.success()
    else:
        status_svc.fail()
        return

    status_svc.start("Loading data and signature files")
    file_map = retrieval_svc.gather()
    status_svc.prog()
    status_svc.success()

    for category, _data in file_map.items():
        status_svc.start(f"Verifying {category.title()} Authenticity", nl=True)
        if category == "timestamps":
            tsq = retrieval_svc.load_file(_data['tsq'])
            tsr = retrieval_svc.load_file(_data['tsr'])
            time_from_tsr = crypto_svc.time_from_tsr(tsr)
            is_authentic = crypto_svc.verify_ts(tsr, tsq)
            status_svc.start(f"{time_from_tsr}")
            status_svc.prog()
            if is_authentic:
                status_svc.success()
            else:
                status_svc.fail()

        else:
            for uuid, packet in _data.items():
                status_svc.start(f"| {uuid} |")

                is_authentic_device = crypto_svc.verified(
                    retrieval_svc.load_file(packet['data']),
                    retrieval_svc.load_file(packet['device']),
                    device_key,
                )
                status_svc.prog(cnt=1)
                is_authentic_verum = crypto_svc.verified(
                    retrieval_svc.load_file(packet['data']),
                    retrieval_svc.load_file(packet['verum']),
                    verum_key,
                )
                status_svc.prog(cnt=1)
                if is_authentic_device and is_authentic_verum:
                    status_svc.prog(cnt=1)
                    status_svc.success()
                else:
                    status_svc.fail()

    if not preserve:
        retrieval_svc.clear()


if __name__ == '__main__':
    main()
